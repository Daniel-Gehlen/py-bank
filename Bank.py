class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if self.saques_diarios < 3 and valor <= 500 and valor <= self.saldo:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_diarios += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > 500:
            print("Limite máximo por saque é de R$ 500.00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite diário de saques atingido.")

    def extrato(self):
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")


# Testando o sistema
banco = Banco()
banco.depositar(1000)
banco.sacar(300)
banco.sacar(600)
banco.sacar(400)
banco.sacar(200)
banco.extrato()
