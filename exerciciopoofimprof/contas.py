from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        ...
    
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f"Depósito {valor}")

    def detalhes(self, msg=""):
        print(f"O seu saldo é {self.saldo:.2f} {msg}")
        print("-------------------")

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencia!r}, {self.conta!r}, {self.saldo!r}"
        return f"{class_name}({attrs})"

    

class ContaPoupanca(Conta):
    def sacar(self, valor):

        if valor > self.saldo:
            self.detalhes("Saldo insuficiente")

        else:
            self.saldo -= valor
            self.detalhes(f"Saque {valor}")
            return self.saldo
        

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo = 0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
    
        if valor > (self.saldo + self.limite):
            self.detalhes("Saldo insuficiente")
            self.detalhes(f"Seu limite maximo é de: {-self.limite:.2f}")
        else:
            self.saldo -= valor
            self.detalhes(f"Saque {valor}")
            return self.saldo
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencia!r},{self.conta!r},{self.saldo!r},{self.limite!r}"
        return f"{class_name}({attrs})"


if __name__ == "__main__":
    cp1 = ContaPoupanca(1111, 2222)
    cp1.sacar(10)
    cp1.depositar(100)
    cp1.sacar(20)

    print("\n--------- Conta Corrente ----------\n")
    cc1 = ContaCorrente(2222, 1111, 0, 400)
    cc1.sacar(40)
    cc1.depositar(200)
    cc1.sacar(600)
