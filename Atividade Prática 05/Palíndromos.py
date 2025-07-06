import string

def eh_palindromo(texto: str) -> str:

    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    # Compara com o texto invertido
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

def main():
    entrada = input("Digite uma palavra ou frase: ")
    resultado = eh_palindromo(entrada)
    print(f"É palíndromo? {resultado}")

main()