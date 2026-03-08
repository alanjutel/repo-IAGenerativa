import json
import os

BASE_DIR = os.path.dirname(__file__) # define o diretório do arquivo json relativo ao script
ARQUIVO_MEMORIA = os.path.join(BASE_DIR, "conversation.json")
LIMITE_MEMORIA = 10


def carregar_memoria():
    if os.path.exists(ARQUIVO_MEMORIA):
        with open(ARQUIVO_MEMORIA, "r") as f:
            return json.load(f)
    return []


def salvar_memoria(historico):
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)


def adicionar_mensagem(historico, mensagem):
    historico.append(mensagem)

    if len(historico) > LIMITE_MEMORIA:
        historico.pop(0)

    salvar_memoria(historico)


def limpar_memoria():
    with open(ARQUIVO_MEMORIA, "w") as f:
        json.dump([], f)