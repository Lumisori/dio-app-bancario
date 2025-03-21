menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
saques_executados = 0
while True:
    opcao = input(menu)
    match opcao:
        case "d":
            valor = float(input("Digite o valor do depósito: R$"))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R${valor:.2f}\n"
            else:
                print("Digite um valor válido.")

        case "s":
            valor = float(input("Digite o valor do saque: R$"))
            if saques_executados >= LIMITE_SAQUES:
                print("Limite de saques diários atingido!")
            elif valor > saldo:
                print("Saldo insuficiente!")
            elif valor <= limite and valor > 0:
                saldo -= valor
                saques_executados += 1
                extrato += f"Saque: R${valor}\n"
            else:
                print("Digite um valor válido")

        case "e":
            print("Extrato".center(50, "="))
            print(
                "Nenhuma movimentação realizada recentemente."
                if not extrato
                else extrato
            )
            print(f"Saldo: R${saldo:.2f}")
            print("=" * 50)

        case "q":
            break

        case _:
            print("Operação inválida, por favor selecione uma operação válida!")
