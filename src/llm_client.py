import ollama
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("OLLAMA_MODEL", "gpt-oss:120b")


class LLMClient:
    def __init__(self):
        self.model = MODEL

    def gerar(self, prompt: str):
        resposta = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return resposta["message"]["content"]
