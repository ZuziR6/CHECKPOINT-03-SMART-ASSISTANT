import json

from src.guardrails import GuardrailSystem
from src.chain import AssistantChain
from src.evaluator import Evaluator


def menu():

    print("=" * 50)
    print("TECHSTORE SMART SUPPORT")
    print("=" * 50)
    print("1 - Modo Interativo")
    print("2 - Rodar Avaliação")

    return input("Escolha: ")


if __name__ == "__main__":

    opcao = menu()

    if opcao == "1":

        guard = GuardrailSystem()
        chain = AssistantChain()

        texto = input("Digite sua solicitação: ")

        seguro, motivo = guard.validar_input(texto)

        if not seguro:
            print(f"Bloqueado: {motivo}")
            exit()

        etapa1 = chain.etapa1_classificar(texto)
        etapa2 = chain.etapa2_processar(etapa1, texto)
        etapa3 = chain.etapa3_responder(etapa2)

        resposta_json = json.dumps(
            etapa3.model_dump(),
            ensure_ascii=False,
            indent=4
        )

        seguro_saida, motivo_saida = guard.validar_output(resposta_json)

        if not seguro_saida:
            print(f"Saída bloqueada: {motivo_saida}")
            exit()

        print(resposta_json)

    elif opcao == "2":

        evaluator = Evaluator()
        evaluator.avaliar()
