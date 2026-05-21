# TechStore Smart Support

Assistente inteligente em Python com prompt chaining, structured output, guardrails e avaliação automática.

## Tecnologias

- Python 3.10+
- Ollama
- Modelo gpt-oss:120b
- Pydantic
- Pandas
- Matplotlib
- Tiktoken

## Instalação

1. Clonar o repositório

```bash
https://github.com/ZuziR6/CHECKPOINT-03-SMART-ASSISTANT
```

2. Criar ambiente virtual

python -m venv venv

3. Ativar ambiente virtual

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate


4. Instalar dependências
   
pip install -r requirements.txt

5. Instalar Ollama

https://ollama.com/download

6. Baixar modelo
   
ollama pull gpt-oss:120b

7. Rodar projeto
python main.py


Funcionalidades

Guardrails de entrada
Prompt chaining
Structured output com Pydantic
Output guards
Avaliação automática
Relatórios CSV
Métricas automáticas


Pipeline

Input → Guardrails → Classificação → Processamento → Resposta → Output Guard
