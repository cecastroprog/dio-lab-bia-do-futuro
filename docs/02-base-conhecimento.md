# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve no Nexus? |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades de aprendizado do cliente |
| `produtos_financeiros.json` | JSON | Conhecer os produtos disponíveis para que eles possam ser ensinados ao cliente. |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e usar essas informações de forma didádica.|
| `feedbacks.csv` | CSV | Analisar feedback do cliente |
| `historico.json` | JSON | Consultar histórico das conversas |
| `metricas.json` | JSON | Registrar métricas de performance |


> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

O 'Fundo Multimercado' foi renomeado para 'Fundo Imobiliário (FII)' para facilitar e ter maior assertividade nas validações devido a familiaridade e conhecimento neste fundo.

Inclusão dos arquivos de dados essenciais: `feedbacks.csv` (contendo os dados dos feedbacks de clientes) e `historico.json` (armazenando o histórico das conversas), que são fundamentais para o funcionamento do agente de análise de feedbacks.

Inclusão do dataset `metricas.json` para o registro de métricas de performance.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt(Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

```python
import json
import pandas as pd
import requests
import streamlit as st
import os
from datetime import datetime
import time

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))
feedbacks = pd.read_csv('./data/feedbacks_clientes.csv')
ARQUIVO_HISTORICO = './data/historico.json'
ARQUIVO_METRICAS = './data/metricas.json'
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
Você é o Nexus, um analista de feedbacks de clientes de institução financeira amigável e didádico.

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
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
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
```
