import textwrap


def exibir_menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def sacar(*, saldo, valor, extrato, saques_executados, limite, LIMITE_SAQUES):
    if saques_executados >= LIMITE_SAQUES:
        print("Limite de saques diários atingido!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    elif 0 < valor <= limite:
        saldo -= valor
        saques_executados += 1
        extrato.append(f"Saque:\t\tR${valor:.2f}")
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Tente novamente.")

    return saldo, extrato, saques_executados


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito:\tR${valor:.2f}")
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido! Tente novamente.")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("=" * 50)
    print("EXTRATO".center(50))
    print("\n".join(extrato) if extrato else "Nenhuma movimentação registrada.")
    print(f"\nSaldo:\t\tR${saldo:.2f}")
    print("=" * 50)


def criar_usuario(usuarios):
    print


def criar_conta_corrente():
    print()


def listar_contas(contas):
    print


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    usuarios = []
    contas = []
    saques_executados = 0

    while True:
        opcao = exibir_menu()

        match opcao:
            case "d":
                valor = float(input("Digite o valor do depósito:R$"))
                saldo, extrato = depositar(saldo, valor, extrato)
            case "s":
                valor = float(input("Digite o valor do saque: R$"))
                saldo, extrato, saques_executados = sacar(
                    saldo=saldo,
                    extrato=extrato,
                    valor=valor,
                    saques_executados=saques_executados,
                    LIMITE_SAQUES=LIMITE_SAQUES,
                    limite=limite,
                )
            case "e":
                exibir_extrato(saldo, extrato=extrato)
            case "q":
                print("Obrigado por usar nosso sistema. Até logo!")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
