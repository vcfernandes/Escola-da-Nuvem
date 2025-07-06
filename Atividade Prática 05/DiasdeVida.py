from datetime import datetime

def calcular_dias_vivo(data_nascimento: str) -> int:
   
    try:
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return None

    hoje = datetime.now()
    dias_vivo = (hoje - nascimento).days
    return dias_vivo

def main():
    print("=== Calculadora de Dias de Vida ===")
    data = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    dias = calcular_dias_vivo(data)

    if dias is not None:
        print(f"Você está vivo há {dias} dias.")

main()