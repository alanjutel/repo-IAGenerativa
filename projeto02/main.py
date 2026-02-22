from classifier import classificar_mensagem
import time

# Mensagens a serem classificadas
mensagens_cliente = [
    "Quero contratar o plano premium",
    "O sistema está com erro",
    "Quero cancelar minha assinatura",
    "Quero falar com um atendente",
    "Preciso de ajuda com meu pagamento",
    "Gostaria de atualizar minhas informações de conta",
    "Vocês trabalham no sábado"
]

temperatura = 1.0 # Tempertura será definida manualmente antes de cada teste (0.1 > 0.6 > 1.0)

for rodada in range(10):
    print(f"\n--- Rodada {rodada + 1} ---\n")

    for mensagem in mensagens_cliente:
        resposta = classificar_mensagem(mensagem, temperature=temperatura)

        print(f"Cliente: {mensagem}")
        print(f"Resposta: {resposta}\n")

        # Delay entre chamadas
        time.sleep(1)