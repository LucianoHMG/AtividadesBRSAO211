def pares_impares():
    print("=== Contador de Pares e Ímpares ===")
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").strip().lower()

        if entrada == "fim":
            break

        try:
            n = int(entrada)
            if n % 2 == 0:
                pares += 1
                print(f"{n} é par.")
            else:
                impares += 1
                print(f"{n} é ímpar.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'fim'.")

    print("\n=== Resultado ===")
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")
    print(f"Total: {pares + impares}")

pares_impares()
# Contador de Números Pares e Ímpares