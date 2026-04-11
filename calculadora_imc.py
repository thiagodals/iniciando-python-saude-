print("Calculadora de Índice de Massa Corporal (IMC) 1.0\n")
peso2 = float(input("Digite seu peso: ").replace(",", "."))
altura = float(input("Digite sua altura: ").replace(",", "."))
imc = peso2 / (altura ** 2)
print(f"Seu IMC é de {imc:.2f}")

while True:
    if imc < 16:
        print("Magreza Grave")
    elif imc < 17:
        print("Magreza Moderada")
    elif imc < 18.5:
        print("Magreza Leve")
    elif imc < 25:
        print("Saudável")
    elif imc < 30:
        print("Sobrepeso")
    elif imc < 35:
        print("Obesidade Grau I")
    elif imc < 40:
        print("Obesidade Grau II")
    else:
        imc > 40
        print("Obesidade Grau III")
    break