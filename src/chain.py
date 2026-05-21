import json

from src.schemas import (
    ClassificacaoSchema,
    ProcessamentoSchema,
    RespostaSchema
)

from src.prompts import (
    PROMPT_CLASSIFICACAO,
    PROMPT_PROCESSAMENTO_RECLAMACAO,
    PROMPT_PROCESSAMENTO_DUVIDA,
    PROMPT_PROCESSAMENTO_ELOGIO,
    PROMPT_RESPOSTA
)

from src.llm_client import LLMClient


class AssistantChain:

    def __init__(self):
        self.llm = LLMClient()

    def etapa1_classificar(self, texto):

        prompt = PROMPT_CLASSIFICACAO.format(texto=texto)

        resposta = self.llm.gerar(prompt)

        dados = json.loads(resposta)

        return ClassificacaoSchema(**dados)

    def etapa2_processar(self, classificacao, texto):

        if classificacao.tipo == "reclamacao":
            prompt = PROMPT_PROCESSAMENTO_RECLAMACAO.format(texto=texto)

        elif classificacao.tipo == "duvida":
            prompt = PROMPT_PROCESSAMENTO_DUVIDA.format(texto=texto)

        else:
            prompt = PROMPT_PROCESSAMENTO_ELOGIO.format(texto=texto)

        resposta = self.llm.gerar(prompt)

        dados = json.loads(resposta)

        return ProcessamentoSchema(**dados)

    def etapa3_responder(self, processamento):

        prompt = PROMPT_RESPOSTA.format(
            dados=processamento.model_dump()
        )

        resposta = self.llm.gerar(prompt)

        dados = json.loads(resposta)

        return RespostaSchema(**dados)
