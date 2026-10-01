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
