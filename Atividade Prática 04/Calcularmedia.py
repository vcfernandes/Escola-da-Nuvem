def registrar_notas():
    alunos = []
    continuar = 's'

    while continuar.lower() == 's':
        nome = input("Digite o nome do aluno: ")
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
        except ValueError:
            print("Nota inválida. Use apenas números.")
            continue

        alunos.append((nome, nota))
        continuar = input("Deseja adicionar outro aluno? (s/n): ")

    if not alunos:
        print("Nenhum aluno foi registrado.")
        return

    soma = sum(nota for _, nota in alunos)
    media = soma / len(alunos)

    print("\n--- Notas dos Alunos ---")
    for nome, nota in alunos:
        print(f"{nome}: {nota}")

    print(f"\nMédia da turma: {media:.2f}")

registrar_notas()