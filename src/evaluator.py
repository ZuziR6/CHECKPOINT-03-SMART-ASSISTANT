import json
import pandas as pd
import matplotlib.pyplot as plt
from src.chain import AssistantChain
from src.guardrails import GuardrailSystem

class Evaluator:
        self.guard = GuardrailSystem()

    def carregar_json(self, caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def avaliar(self):

        testes = self.carregar_json("data/test_dataset.json")
        ataques = self.carregar_json("data/attack_dataset.json")

        classificacoes_corretas = 0
        jsons_validos = 0
        ataques_bloqueados = 0
        falsos_positivos = 0

        resultados = []

        for teste in testes:

            texto = teste["texto"]

            seguro, motivo = self.guard.validar_input(texto)

            if not seguro:
                falsos_positivos += 1
                continue

            try:
                etapa1 = self.chain.etapa1_classificar(texto)

                if etapa1.tipo == teste["tipo_esperado"]:
                    classificacoes_corretas += 1

                etapa2 = self.chain.etapa2_processar(etapa1, texto)
                etapa3 = self.chain.etapa3_responder(etapa2)

                jsons_validos += 1

                resultados.append({
                    "texto": texto,
                    "tipo": etapa1.tipo,
                    "urgencia": etapa1.urgencia,
                    "resposta": etapa3.resposta
                })

            except:
                pass

        for ataque in ataques:

            seguro, _ = self.guard.validar_input(ataque["texto"])

            if not seguro:
                ataques_bloqueados += 1

        total_testes = len(testes)
        total_ataques = len(ataques)

        metricas = {
            "acuracia": round((classificacoes_corretas / total_testes) * 100, 2),
            "json_valido": round((jsons_validos / total_testes) * 100, 2),
            "bloqueio": round((ataques_bloqueados / total_ataques) * 100, 2),
            "falso_positivo": round((falsos_positivos / total_testes) * 100, 2)
        }

        df = pd.DataFrame(resultados)

        df.to_csv("output/eval_results.csv", index=False)

        plt.figure(figsize=(8, 5))
        plt.bar(metricas.keys(), metricas.values())
        plt.ylabel("Porcentagem")
        plt.title("Métricas de Avaliação")
        plt.savefig("output/graficos/grafico_metricas.png")

        print("Métricas:")
        print(metricas)
