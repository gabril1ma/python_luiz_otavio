from abc import ABC, abstractmethod


class Conta(ABC):
    
    def ContaCorrente(self, numero, agencia, saldo):
        ...
    
    def ContaPoupanca(self, numero, agencia, saldo):
        ...

class Pessoa(ABC):
    ...


class Cliente(Pessoa):
    ...


class ContaPoupanca(Conta):
    ...


class ContaCorrente(Conta):
    ...

class Banco:
    ...
