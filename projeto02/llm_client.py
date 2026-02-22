from groq import Groq
import os
from dotenv import load_dotenv
import time

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key=groq_api_key,
    timeout=30  # timeout global da conexão
)


def gerar_resposta(prompt, temperature=0.2, max_retries=3):
    """
    Gera resposta a partir do prompt usando o modelo Groq.
    Inclui timeout e retry automático.
    """

    for tentativa in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=50  # limita resposta
            )

            return chat_completion.choices[0].message.content

        except Exception as e:
            print(f"[Tentativa {tentativa + 1}] Erro: {e}")
            time.sleep(1)

    # fallback seguro se falhar todas as tentativas
    return '{"categoria": "Geral"}'