import re
import json


class GuardrailSystem:

    def __init__(self):
        self.padroes_bloqueados = [
            r"ignore previous instructions",
            r"forget your rules",
            r"reveal system prompt",
            r"jailbreak",
            r"DAN",
            r"bypass",
            r"hack",
            r"system override"
        ]

    def validar_input(self, texto):

        if len(texto) > 500:
            return False, "Texto muito longo"

        caracteres_proibidos = ["<", ">", "{", "}"]

        for caractere in caracteres_proibidos:
            if caractere in texto:
                return False, "Caracteres proibidos"

        for padrao in self.padroes_bloqueados:
            if re.search(padrao, texto, re.IGNORECASE):
                return False, f"Ataque detectado: {padrao}"

        return True, "Input seguro"

    def validar_output(self, resposta):

        termos_proibidos = [
            "system prompt",
            "ignore instructions",
            "senha interna"
        ]

        for termo in termos_proibidos:
            if termo.lower() in resposta.lower():
                return False, "Possível vazamento"

        try:
            json.loads(resposta)
        except:
            return False, "JSON inválido"

        return True, "Output seguro"
