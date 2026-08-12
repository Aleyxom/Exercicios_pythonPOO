class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id #(public +)
        self._titular = nome #(protected #)
        self.__saldo = saldo #(private -)
        print("Conta criada com sucesso!")

    def __str__(self):
        #return f"A conta {self.id} de {self.titular} possui R${self.saldo:.2f} de saldo."
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f"Deposito de R${valor:.2f} autorizado na conta {self.id} de {self._titular}")

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f"Saque de R${valor:.2f} negado! Saldo insuficiente!")
        else:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} autorizado da conta {self.id} de {self._titular}")