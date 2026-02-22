from llm_client import gerar_resposta
from validator import processar_resposta_modelo

CATEGORIAS = ["Suporte", "Vendas", "Financeiro", "Geral"]


def classificar_mensagem(mensagem, temperature=0.2):
    """
    Classifica uma mensagem em uma das categorias definidas.
    Retorna um dicionário validado.
    """
    prompt = f"""
Classifique a mensagem abaixo em uma das seguintes categorias: {', '.join(CATEGORIAS)}.
Retorne apenas um JSON no formato:
{{
    "categoria": "nome_categoria"
}}

Mensagem: "{mensagem}"
"""

    resposta_modelo = gerar_resposta(prompt, temperature)

    # Passa pelo pipeline de validação
    resultado_final = processar_resposta_modelo(resposta_modelo, CATEGORIAS)

    return resultado_final