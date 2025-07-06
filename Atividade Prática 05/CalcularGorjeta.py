def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta


def main():
    print("=== Calculadora de Gorjeta ===")
    try:
        valor_conta = float(input("Digite o valor total da conta (R$): "))
        porcentagem = float(input("Digite a porcentagem da gorjeta (%): "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        return

    valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    total_a_pagar = valor_conta + valor_gorjeta

    print(f"\nValor da conta: R${valor_conta:.2f}")
    print(f"Gorjeta ({porcentagem:.0f}%): R${valor_gorjeta:.2f}")
    print(f"Total a pagar: R${total_a_pagar:.2f}")


main()