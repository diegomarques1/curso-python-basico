class Banco:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
    
    def deposito(self, valor):
        self.saldo += valor

    def saque(self, valor):
        self.saldo -= valor

    def transferencia(self, outra_conta, valor):
        self.saldo -= valor
        outra_conta.saldo += valor

conta_diego = Banco("Diego", 1000)
conta_julia = Banco("Júlia", 1500)

conta_diego.deposito(1000)
print(conta_diego.saldo)

conta_diego.saque(500)
print(conta_diego.saldo)

conta_julia.transferencia(conta_diego, 250)
print(conta_diego.saldo)
print(conta_julia.saldo)