from llm_client import LLMClient
from retriever import load_conhecimento, similarity_search
from validator import validate_json, detect_prompt_injection
from prompt import build_system_prompt


def main():
    provider = input("Escolha o provedor (openai/groq): ").strip().lower()
    client = LLMClient(provider=provider)

    # Carrega conhecimento e gera embeddings uma única vez
    load_conhecimento()

    while True:
        query = input("Digite sua pergunta (ou 'sair' para encerrar): ").strip()

        if query.lower() == "sair":
            break

        # PROTEÇÃO PROMPT INJECTION
        if detect_prompt_injection(query):
            print("⚠️ Solicitação bloqueada por violar regras de segurança.")
            continue

        # BUSCA SEMÂNTICA (EMBEDDINGS)
        contexto = similarity_search(query)

        system_prompt = build_system_prompt()

        user_prompt = f"""
Pergunta do usuário:
{query}

Contexto recuperado da base de conhecimento:
{contexto}

Responda APENAS em JSON conforme instruído.
"""

        response_text = client.generate_text(system_prompt, user_prompt)

        # VALIDAÇÃO DE JSON
        try:
            is_valid, data = validate_json(response_text)

            if is_valid:
                if data["status"] == "sucesso":
                    print(f"Resposta: {data['resposta']}")
                else:
                    print("Resposta: Informação não encontrada na base de conhecimento.")

        except ValueError as e:
            print("⚠️ Erro de validação do modelo.")
            print("Resposta bruta recebida:")
            print(response_text)


if __name__ == "__main__":
    main()