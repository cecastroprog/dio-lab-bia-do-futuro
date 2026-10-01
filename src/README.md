# Passo a Passo de Execução

## Setup do Ollama

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve
ollama pull gpt-oss

# 3. Testar se funciona
ollama run llama3.2 "Olá!"
```

## Código Completo

Todo o código-fonte esta no arquivo `app.py`

## Como Rodar

```bash
# 1. Instalar dependências
pip install stream pandas requests

# 2. Garantir que Ollama está rodando
ollama serve

# Rodar o app
streamlit run app.py
```

## Evidência de Execução

<img width="1148" height="957" alt="evidencia_questionar_detalhes" src="https://github.com/user-attachments/assets/95e4e116-54af-4c77-b0a9-f7c6bea9e0e3" />
