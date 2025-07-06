def analisar_numeros():
    pares = 0
    impares = 0

    print("Digite números para analisar (digite 'sair' para encerrar):")

    while True:
        entrada = input("Número: ")

        if entrada.lower() == 'sair':
            break

        try:
            numero = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro ou 'sair'.")
            continue

        if numero % 2 == 0:
            print(f"{numero} é PAR.")
            pares += 1
        else:
            print(f"{numero} é ÍMPAR.")
            impares += 1

    print("\n--- Resultado Final ---")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")


analisar_numeros()