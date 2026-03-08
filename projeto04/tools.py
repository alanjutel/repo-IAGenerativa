import datetime
import random
import string


def data_atual():
    return datetime.date.today()


def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    return ano_atual - int(ano_nascimento)


def converter_temperatura(valor, origem, destino):
    valor = float(valor)

    if origem == "c" and destino == "f":
        return (valor * 9/5) + 32
    elif origem == "f" and destino == "c":
        return (valor - 32) * 5/9
    else:
        return "Conversão não suportada."


def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha