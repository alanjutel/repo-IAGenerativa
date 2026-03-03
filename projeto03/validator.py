import json
import re


def validate_json(response_text):
    try:
        data = json.loads(response_text)
        if "status" not in data:
            raise ValueError("Campo 'status' obrigatório")
        if "resposta" not in data:
            raise ValueError("Campo 'resposta' obrigatório")
        return True, data
    except json.JSONDecodeError as e:
        raise ValueError(f"Erro ao decodificar JSON: {e}")


def detect_prompt_injection(query):
    injection_patterns = [
        r"ignore",
        r"esqueça",
        r"esqueca",
        r"system prompt",
        r"instruções internas",
        r"qual sua system",
        r"reveal",
        r"mostre suas instruções",
    ]

    query_lower = query.lower()

    for pattern in injection_patterns:
        if re.search(pattern, query_lower):
            return True

    return False