def eh_bissexto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

try:
    ano = int(input("Digite um ano: "))
    
    if eh_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")