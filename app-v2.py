class Banco:
    def __init__(self):
        self.saldo = 0
        self.extrato = ""
        self.saques_executados = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_VALOR_SAQUE = 500

    def depositar(self, valor: float) -> None:
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R${valor:.2f}\n"
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor: float) -> None:
        if self.saques_executados >= self.LIMITE_SAQUES:
            print("Erro: Limite diário de saques atingido.")
        elif valor > self.saldo:
            print("Erro: Saldo insuficiente.")
        elif valor > self.LIMITE_VALOR_SAQUE:
            print(
                f"Erro: O valor do saque não pode exceder R${self.LIMITE_VALOR_SAQUE:.2f}."
            )
        elif valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        else:
            self.saldo -= valor
            self.saques_executados += 1
            self.extrato += f"Saque: R${valor:.2f}\n"
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def exibir_extrato(self) -> None:
        print(" EXTRATO ".center(50, "="))
        if not self.extrato:
            print("Nenhuma movimentação realizada recentemente.")
        else:
            print(self.extrato)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("=" * 50)


def obter_valor_numerico(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: Por favor, insira um valor numérico válido.")


def main():
    banco = Banco()
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
=> """

    while True:
        opcao = input(menu).strip().lower()
        match opcao:
            case "d":
                valor = obter_valor_numerico("Digite o valor do depósito: R$")
                banco.depositar(valor)
            case "s":
                valor = obter_valor_numerico("Digite o valor do saque: R$")
                banco.sacar(valor)
            case "e":
                banco.exibir_extrato()
            case "q":
                print("Saindo do sistema. Até logo!")
                break
            case _:
                print("Operação inválida. Por favor, selecione uma operação válida.")


if __name__ == "__main__":
    main()