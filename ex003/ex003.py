class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print("Conta criada com sucesso!")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} possui R${self.saldo:.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self.id} de {self.titular}")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:.2f} negado! Saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado da conta {self.id} de {self.titular}")

c1 = ContaBancaria(112, "Aleyxom Carlos", 3000)
c1.depositar(500)
c1.sacar(450)
c1.sacar(3000000)
print(c1)