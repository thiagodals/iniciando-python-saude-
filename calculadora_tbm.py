print("Calculadora de Taxa de Metabolismo Basal (TMB)\n")

while True:
    idade = int(input("Digite sua idade: "))

    if 18 <= idade <= 30:
        print("Escolha uma opção:")
        print("Homem")
        print("Mulher")

        opcao = input("H ou M:").upper()
        
        while opcao in ("H","M"):

            if opcao == "H":
                peso = float(input("Digite seu peso: "))
                tbm = (15.057 * peso) + 692.2
                print(f"Seu TBM é de {tbm:.2f}")
                break

            if opcao == "M":
                peso = float(input("Digite seu peso: "))
                tbm = (14.818 * peso) + 486.6
                print(f"Seu TBM é de {tbm:.2f}")
                break

    else:
        print("Idade fora da faixa (18 a 30 anos)")

    resposta = input("Deseja calcular novamente? (S/N): ").upper()
    if resposta != "S":
        break