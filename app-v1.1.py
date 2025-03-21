def exibir_menu():
    return """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """


def depositar(saldo, extrato):
    valor = float(input("Digite o valor do depósito: R$"))
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Tente novamente.")
    return saldo, extrato


def sacar(saldo, extrato, saques_executados, LIMITE_SAQUES, LIMITE_SAQUE):
    valor = float(input("Digite o valor do saque: R$"))

    if saques_executados >= LIMITE_SAQUES:
        print("Limite de saques diários atingido!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif 0 < valor <= LIMITE_SAQUE:
        saldo -= valor
        saques_executados += 1
        extrato.append(f"Saque: R${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Tente novamente.")

    return saldo, extrato, saques_executados


def exibir_extrato(saldo, extrato):
    print("=" * 50)
    print("EXTRATO".center(50))
    print("\n".join(extrato) if extrato else "Nenhuma movimentação registrada.")
    print(f"\nSaldo atual: R${saldo:.2f}")
    print("=" * 50)


def main():
    saldo = 0
    extrato = []
    LIMITE_SAQUE = 500
    LIMITE_SAQUES = 3
    saques_executados = 0

    while True:
        opcao = input(exibir_menu()).strip().lower()

        match opcao:
            case "d":
                saldo, extrato = depositar(saldo, extrato)
            case "s":
                saldo, extrato, saques_executados = sacar(
                    saldo, extrato, saques_executados, LIMITE_SAQUES, LIMITE_SAQUE
                )
            case "e":
                exibir_extrato(saldo, extrato)
            case "q":
                print("Obrigado por usar nosso sistema. Até logo!")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
