from abc import ABC, abstractmethod

class Conta(ABC):
    
    def __init__(self, numero, agencia, saldo):
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo  
        self.limite = 1
    
    def get_saldo(self):
        return self.saldo

    def get_conta(self):
        return self.numero
    
    def get_agencia(self):
        return self.agencia

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
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade
class Cliente(Pessoa):

    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

    def definir_conta(self):
        return self.conta
    
class ContaPoupanca(Conta):
    def sacar(self, valor):
        return super().sacar(valor)


class ContaCorrente(Conta):


    def sacar(self, valor):
        return super().sacar(valor)
    
    def __init__(self, agencia, numero, saldo, limite):
        super().__init__(numero, agencia, saldo)
        self.limite = limite
    
    def definir_limite(self):
        self.limite = self.saldo * 1.2

class Banco:

    def __init__(self):
        self.clientes = []
        self.contas = []

 
    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_contas(self, conta):
        self.contas.append(conta)

    def listar_contas(self):

        for i in self.contas():
            print(i)

    def autenticar(self, cliente, conta, agencia):
        if cliente.conta.numero == conta and cliente.conta.agencia == agencia:
            return True
        else:
            return False


banco = Banco()
 
conta1 = ContaCorrente("001", "12345", 1000.0, 500.0)
conta2 = ContaPoupanca("001", "67890", 2000.0)
 
cliente1 = Cliente("João Henrique", 30, conta1)
cliente2 = Cliente("Maria Vitória", 25, conta2)
 
banco.adicionar_contas(conta1)
banco.adicionar_contas(conta2)
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
 
# Autenticação do banco
cliente = cliente1
conta = cliente.definir_conta()
agencia = conta.get_agencia()
 
if banco.autenticar(cliente, conta, agencia):
    valor_saque = 1000.0
    if conta.sacar(valor_saque):
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente para saque.")
else:
    print("Autenticação falhou.")