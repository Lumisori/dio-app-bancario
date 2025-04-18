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


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Este CPF já foi cadastrado no sistema!")
        return
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        "Informe seu endereço (logradouro, numero - bairro - cidade/estado): "
    )
    usuarios.append(
        {"nome": nome, "data_nascimento": data_nasc, "cpf": cpf, "endereço": endereco}
    )
    print("@@@@ Usuário criado com sucesso! @@@@")


def criar_conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente números)")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("@@@@ Conta Corrente criada com sucesso ! @@@@")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print(
        "\n @@@@ Usuário não encontrado no sistema, cadastre um novo CPF ao sistema! @@@@"
    )


def listar_contas(contas):
    if contas:
        for conta in contas:
            linha = f"""
                Agência:\t {conta['agencia']}
                Conta Corrente:\t {conta['numero_conta']}
                Titular:\t {conta['usuario']['nome']}
            """
            print("=" * 50)
            print(textwrap.dedent(linha))
    else:
        print("@@@@ Nenhuma conta corrente cadastrada no sistema! @@@@")
        return


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
            case "nu":
                criar_usuario(usuarios)
            case "nc":
                numero_conta = len(contas) + 1
                conta = criar_conta_corrente(AGENCIA, numero_conta, usuarios)
                if conta:
                    contas.append(conta)
            case "lc":
                listar_contas(contas)
            case "q":
                print("Obrigado por usar nosso sistema. Até logo!")
                break
            case _:
                print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
