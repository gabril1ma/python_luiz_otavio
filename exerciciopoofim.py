from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo  
        self._limite = 0

    def definir_limite(self, saldo):
        self._limite = saldo * 1.3
        

    def Depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        if valor > self.saldo:
            print("Saldo insuficiente")

        self.saldo -= valor

class Pessoa(ABC):
    def __init__(self):
        self._nome = None
        self._idade = None

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, value):
        self._idade = value

class Cliente(Pessoa):
    
    def definir_conta(self, conta):
        self.conta = conta


c1 = Cliente()
c1.nome = "Gabriel"
c1.idade = 20

class ContaPoupanca(Conta):
    def sacar(self, valor):
        return super().sacar(valor)


class ContaCorrente(Conta):

    def sacar(self, valor):
        return super().sacar(valor)
    
    def __init__(self):
        self._limite *= 1.2

class Banco:

    def __init__(self):

        self.contas = None

    def listar_contas(self):

        for i in self.conta():
            print(i)

