from groq import Groq
from dotenv import load_dotenv
import os
import re

from tools import data_atual, calcular_idade, converter_temperatura, gerar_senha
from memory_manager import carregar_memoria, adicionar_mensagem, limpar_memoria

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Persona do assistente
SYSTEM_PROMPT = """
Você é um assistente virtual educado, claro e prestativo.
Sempre responda de forma objetiva e amigável.

Você pode ajudar com:
- responder perguntas gerais
- cálculos simples
- conversão de temperatura
- cálculo de idade
- geração de senhas seguras

Se uma pergunta exigir cálculo, use a função apropriada.
"""

historico_mensagens = carregar_memoria()

# adiciona system prompt apenas se histórico estiver vazio
if not historico_mensagens:
    historico_mensagens.append({"role": "system", "content": SYSTEM_PROMPT})


def chat(pergunta):

    adicionar_mensagem(historico_mensagens, {"role": "user", "content": pergunta})

    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=historico_mensagens
    )

    resposta_conteudo = resposta.choices[0].message.content

    adicionar_mensagem(
        historico_mensagens,
        {"role": "assistant", "content": resposta_conteudo}
    )

    return resposta_conteudo


def detectar_funcoes(pergunta):

    pergunta_lower = pergunta.lower()

    # Data atual
    if "data" in pergunta_lower:
        return "Hoje é " + str(data_atual())

    # Calcular idade
    match_idade = re.search(r"nasci em (\d{4})", pergunta_lower)
    if match_idade:
        ano = match_idade.group(1)
        idade = calcular_idade(ano)
        return f"Você tem aproximadamente {idade} anos."

    # Conversão temperatura
    match_temp = re.search(r"(\d+)\s*c.*f", pergunta_lower)
    if match_temp:
        valor = match_temp.group(1)
        resultado = converter_temperatura(valor, "c", "f")
        return f"{valor}°C equivalem a {resultado:.2f}°F."

    # Gerar senha
    if "gerar senha" in pergunta_lower or "senha segura" in pergunta_lower:
        senha = gerar_senha()
        return f"Sua senha segura é: {senha}"

    return None


while True:

    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    # limpar memória
    if pergunta.lower() == "/limpar":
        limpar_memoria()
        historico_mensagens.clear()
        historico_mensagens.append({"role": "system", "content": SYSTEM_PROMPT})
        print("Assistente: Memória da conversa apagada.")
        continue

    # verificar funções
    resposta_funcao = detectar_funcoes(pergunta)

    if resposta_funcao:
        adicionar_mensagem(historico_mensagens, {"role": "user", "content": pergunta})
        adicionar_mensagem(
            historico_mensagens,
            {"role": "assistant", "content": resposta_funcao}
        )
        print("Assistente:", resposta_funcao)
        continue

    resposta = chat(pergunta)

    print("Assistente:", resposta)