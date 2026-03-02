class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
    def __str__(self):
        return f"A conta {self.id} de {self.titular}, tem R${self.saldo:,.2f} de saldo"
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor:,.2f} foi autorizado na conta {self.id}")
        print(f"O valor na conta {self.id} é R${self.saldo:,.2f}")
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE  ')
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} foi autorizado na conta {self.id}")
            print(f"O valor na conta {self.id} é R${self.saldo:,.2f}")

c1 = ContaBancaria(121, "Miguel", 5000)
c1.depositar(500)
c1.sacar(10000)
print(c1)

