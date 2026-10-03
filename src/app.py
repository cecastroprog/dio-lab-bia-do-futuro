import json
import pandas as pd
import requests
import streamlit as st
import os
from datetime import datetime
import time

# ========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"

# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
feedbacks = pd.read_csv('./data/feedbacks_clientes.csv')

# ========== HISTÓRICO DE CONVERSAS (JSON) ==========
ARQUIVO_HISTORICO = './data/historico.json'

def _ler_historico():
    """Lê o arquivo; se não existir ou estiver corrompido, retorna lista vazia."""
    if not os.path.exists(ARQUIVO_HISTORICO):
        return []
    try:
        with open(ARQUIVO_HISTORICO, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return []

def _salvar_historico(dados):
    with open(ARQUIVO_HISTORICO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def gravar_historico(pergunta, resposta):
    """Adiciona uma nova interação ao histórico."""
    dados = _ler_historico()
    novo_id = max((item['id'] for item in dados), default=0) + 1
    dados.append({
        "id": novo_id,
        "data_hora": datetime.now().isoformat(timespec='seconds'),
        "pergunta": pergunta,
        "resposta": resposta
    })
    _salvar_historico(dados)

def consultar_historico(ultimas=5):
    """Retorna as últimas N interações."""
    return _ler_historico()[-ultimas:]

def excluir_historico(id_item=None):
    """Exclui um item pelo id; se id_item for None, limpa tudo."""
    if id_item is None:
        _salvar_historico([])
    else:
        _salvar_historico([i for i in _ler_historico() if i['id'] != id_item])

def formatar_historico(ultimas=5):
    """Transforma as últimas interações em texto para o prompt."""
    itens = consultar_historico(ultimas)
    if not itens:
        return "Nenhuma interação anterior nesta conversa."
    return "\n".join(
        f"Cliente: {i['pergunta']}\nNexos: {i['resposta']}\n"
        for i in itens
    )

# ========== MÉTRICAS DE PERFORMANCE ==========
ARQUIVO_METRICAS = './data/metricas.json'
ultima_resposta_ollama = {}   # guarda os dados técnicos da última chamada

def calcular_metricas(tempo_total):
    d = ultima_resposta_ollama
    geracao_s = d.get('eval_duration', 0) / 1e9
    tokens_saida = d.get('eval_count', 0)
    return {
        "data_hora": datetime.now().isoformat(timespec='seconds'),
        "tempo_total_s": round(tempo_total, 2),
        "carga_modelo_s": round(d.get('load_duration', 0) / 1e9, 2),
        "leitura_prompt_s": round(d.get('prompt_eval_duration', 0) / 1e9, 2),
        "geracao_s": round(geracao_s, 2),
        "tokens_entrada": d.get('prompt_eval_count', 0),
        "tokens_saida": tokens_saida,
        "tokens_por_s": round(tokens_saida / geracao_s, 1) if geracao_s else 0,
    }

def gravar_metrica(metrica):
    try:
        with open(ARQUIVO_METRICAS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
    except (OSError, json.JSONDecodeError):
        dados = []
    dados.append(metrica)
    with open(ARQUIVO_METRICAS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def resumo_metricas():
    """Média, mediana e máximo de cada métrica numérica."""
    try:
        with open(ARQUIVO_METRICAS, 'r', encoding='utf-8') as f:
            df = pd.DataFrame(json.load(f))
    except (OSError, json.JSONDecodeError):
        return None
    if df.empty:
        return None
    return df.drop(columns=['data_hora']).agg(['mean', 'median', 'max']).T.round(2)

def carregar_metricas_df(ultimas=10):
    """Carrega as últimas N métricas como DataFrame (P1, P2... no índice)."""
    try:
        with open(ARQUIVO_METRICAS, 'r', encoding='utf-8') as f:
            df = pd.DataFrame(json.load(f))
    except (OSError, json.JSONDecodeError):
        return None
    if df.empty:
        return None
    df = df.tail(ultimas).reset_index(drop=True)
    df.index = [f"P{i+1:02d}" for i in range(len(df))]
    return df

def limpar_metricas():
    """Apaga todas as métricas gravadas."""
    with open(ARQUIVO_METRICAS, 'w', encoding='utf-8') as f:
        json.dump([], f)

# ========== MONTAR CONTEXTO ==========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

FEEDBACKS_CLIENTES:
{feedbacks.to_string(index=False)}
"""

# ========== SYSTEM PROMPT ==========
SYSTEM_PROMPT = """Você é o Nexos, um analista de feedbacks de clientes de institução financeira amigável e didádico.

OBJETIVO:
Demonstrar analises de feedbacks de forma simples, usando os dados de clientes como exemplos práticos.

REGRAS:
- NUNCA sugira um plano de ação;
- NUNCA recomente investimentos específicos, apenas explique como funcionam;
- JAMAIS responda a perguntas fora do tema feedback. 
  Quando ocorrer, responda lembrando o seu papel de analista de feedback de clientes;
- Use os dados fornecidos para dar exemplos personalizados;
- Linguagem simples, como se explicasse para um amigo;
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar...";
- Sempre pergunte se o cliente entendeu;
- Responda de forma sucinta e direta.
"""

# ========= CHAMAR OLLAMA =========
def perguntar(msg):
    historico_conversa = formatar_historico()   

    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    HISTÓRICO DA CONVERSA (usado para responder perguntas de acompanhamento):
    {historico_conversa}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    ultima_resposta_ollama.update(r.json())   
    return r.json()['response']

# ========== INTERFACE =========
st.title("Nexus, Seu Analista de Feedbacks de Clientes")

if pergunta := st.chat_input("Sua dúvida sobre feedbacks..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        inicio = time.perf_counter()                      
        resposta = perguntar(pergunta)
        tempo_total = time.perf_counter() - inicio        
        st.chat_message("assistant").write(resposta)
        gravar_historico(pergunta, resposta)
        metrica = calcular_metricas(tempo_total)          
        gravar_metrica(metrica)                           
        st.caption(f"⏱ {metrica['tempo_total_s']}s | "    
                   f"{metrica['tokens_entrada']} tokens entrada | "
                   f"{metrica['tokens_por_s']} tokens/s")

# resumo na barra lateral
resumo = resumo_metricas()
if resumo is not None:
    st.sidebar.subheader("Métricas de performance")
    st.sidebar.dataframe(resumo)

# ========== BOTÕES: GRÁFICO E LIMPEZA ==========
st.sidebar.divider()

# Botão que abre/fecha o gráfico
if st.sidebar.button("📊 Abrir/fechar gráfico de métricas"):
    st.session_state['mostrar_grafico'] = not st.session_state.get('mostrar_grafico', False)

# Botão que limpa histórico e métricas (com confirmação para evitar clique acidental)
confirmar = st.sidebar.checkbox("Confirmar limpeza")
if st.sidebar.button("🗑️ Limpar histórico e métricas", disabled=not confirmar):
    excluir_historico()
    limpar_metricas()
    st.session_state['mostrar_grafico'] = False
    st.session_state['limpou'] = True
    st.rerun()

if st.session_state.pop('limpou', False):
    st.sidebar.success("Histórico e métricas apagados.")

# Gráfico
if st.session_state.get('mostrar_grafico'):
    df_graf = carregar_metricas_df()
    if df_graf is None:
        st.info("Ainda não há métricas para exibir.")
    else:
        st.subheader("Métricas de performance (últimas 10 perguntas)")
        st.caption("Tempo por pergunta, em segundos")
        st.bar_chart(df_graf[['carga_modelo_s', 'leitura_prompt_s', 'geracao_s']])
        st.caption("Tokens de entrada e saída")
        st.line_chart(df_graf[['tokens_entrada', 'tokens_saida']])

