def verificar_senha(senha):
    if len(senha) < 8:
        return "Senha muito curta! Deve ter pelo menos 8 caracteres."

    if not any(char.isdigit() for char in senha):
        return "A senha deve conter pelo menos um número."

    return "Senha válida!"

senha_usuario = input("Digite sua senha: ")
resultado = verificar_senha(senha_usuario)
print(resultado)