def calcular_desconto(preco_original: float, porcentagem_desconto: float) -> float:

    return preco_original * (porcentagem_desconto / 100)

def calcular_preco_final(preco_original: float, desconto: float) -> float:

    return preco_original - desconto

def main():
    print("=== Calculadora de Desconto ===")
    
    try:
        preco = float(input("Digite o preço original do produto (R$): "))
        porcentagem = float(input("Digite a porcentagem de desconto (%): "))
    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números.")
        return

    desconto = calcular_desconto(preco, porcentagem)
    preco_final = calcular_preco_final(preco, desconto)

    print("\n--- Resultado ---")
    print(f"Preço original: R${preco:.2f}")
    print(f"Desconto ({porcentagem:.0f}%): R${desconto:.2f}")
    print(f"Preço final: R${preco_final:.2f}")


main()