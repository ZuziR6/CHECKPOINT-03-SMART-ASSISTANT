PROMPT_CLASSIFICACAO = """
        "categoria": "duvida"
    }},
    "analise": "",
    "sentimento": "neutro"
}}
"""


PROMPT_PROCESSAMENTO_ELOGIO = """
Você é um analista de experiência do cliente.

Texto:
{texto}

Retorne JSON:
{{
    "dados_extraidos": {{
        "tipo": "elogio"
    }},
    "analise": "",
    "sentimento": "positivo"
}}
"""


PROMPT_RESPOSTA = """
CRISPE FRAMEWORK

Capacity:
Você possui experiência em atendimento premium.

Role:
Você é especialista da TechStore.

Insight:
Dados extraídos:
{dados}

Statement:
Gere uma resposta clara e objetiva.

Personality:
Tom profissional, educado e empático.

Experiment:
Sugira a melhor ação possível.

Retorne JSON:
{{
    "resposta": "",
    "confianca": "alta|media|baixa",
    "acao_sugerida": ""
}}
"""
