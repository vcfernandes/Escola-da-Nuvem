peso = float(input("Por favor, digite seu peso em kg: "))
altura = float(input("Por favor, digite sua altura em metros: "))

imc = peso / (altura ** 2)


if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"


print("\n--- Resultado do seu IMC ---")
print(f"Seu peso: {peso:.2f} kg")
print(f"Sua altura: {altura:.2f} m")
print(f"Seu IMC é: {imc:.2f}") 
print(f"Classificação: {classificacao}")