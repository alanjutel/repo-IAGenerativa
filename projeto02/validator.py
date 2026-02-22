import json
from typing import Dict, Any


def parse_json_resposta(resposta: str) -> Dict[str, Any]:
    """
    Tenta converter a resposta do modelo para JSON.
    Remove possíveis blocos ```json ``` se existirem.
    """
    try:
        resposta_limpa = resposta.strip()

        # Remove markdown se o modelo retornar ```json
        if resposta_limpa.startswith("```"):
            resposta_limpa = resposta_limpa.replace("```json", "")
            resposta_limpa = resposta_limpa.replace("```", "")
            resposta_limpa = resposta_limpa.strip()

        return json.loads(resposta_limpa)

    except json.JSONDecodeError as e:
        raise ValueError(f"JSON inválido: {e}")

    except Exception as e:
        raise ValueError(f"Erro inesperado ao fazer parse do JSON: {e}")


def validar_categoria(dados: Dict[str, Any], categorias_permitidas: list) -> Dict[str, Any]:
    """
    Verifica se o JSON contém a chave correta e se a categoria é válida.
    """
    try:
        if "categoria" not in dados:
            raise ValueError("Campo 'categoria' não encontrado no JSON.")

        categoria = dados["categoria"]

        if categoria not in categorias_permitidas:
            raise ValueError(f"Categoria inválida: {categoria}")

        return dados

    except Exception as e:
        raise ValueError(f"Erro na validação da categoria: {e}")


def fallback_seguro() -> Dict[str, str]:
    """
    Fallback padrão caso o modelo falhe.
    """
    return {"categoria": "Geral"}


def processar_resposta_modelo(resposta: str, categorias_permitidas: list) -> Dict[str, str]:
    """
    Pipeline completo:
    - Parse JSON
    - Validar categoria
    - Aplicar fallback se necessário
    """
    try:
        dados = parse_json_resposta(resposta)
        dados_validados = validar_categoria(dados, categorias_permitidas)
        return dados_validados

    except Exception as e:
        print(f"[ERRO] {e}")
        return fallback_seguro()