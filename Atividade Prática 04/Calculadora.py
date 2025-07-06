def calculadora():
    print("Calculadora Simples em Python")
    print("Operações disponíveis:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    operacao = input("Escolha a operação (1/2/3/4): ")

    if operacao not in ['1', '2', '3', '4']:
        print("Operação inválida!")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    if operacao == '1':
        resultado = num1 + num2
        simbolo = '+'
    elif operacao == '2':
        resultado = num1 - num2
        simbolo = '-'
    elif operacao == '3':
        resultado = num1 * num2
        simbolo = '*'
    elif operacao == '4':
        if num2 == 0:
            print("Erro: divisão por zero!")
            return
        resultado = num1 / num2
        simbolo = '/'

    print(f"\nResultado: {num1} {simbolo} {num2} = {resultado}")
    
calculadora()