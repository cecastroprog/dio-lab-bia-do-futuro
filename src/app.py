import json
import pandas as pd
import requests
import streamlit as st

# ========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama3.2"

# ========== CARREGAR DADOS ==========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
feedbacks = pd.read_csv('./data/feedbacks_clientes.csv')

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
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ========== INTERFACE =========
st.title("Nexus, Seu Analista de Feedbacks de Clientes")

if pergunta := st.chat_input("Sua dúvida sobre feedbacks..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
