from abc import ABC, abstractmethod
 
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade
 
class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0.0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo
    
    def get_agencia(self):
        return self._agencia
    
    def get_numero_conta(self):
        return self._numero_conta
    
    def get_saldo(self):
        return self._saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass
    
    def depositar(self, valor):
        self._saldo += valor
 
class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0.0, limite=0.0):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite
    
    def get_limite(self):
        return self._limite
    
    def sacar(self, valor):
        if self._saldo + self._limite >= valor:
            self._saldo -= valor
            return True
        else:
            return False
 
class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        else:
            return False
 
class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self._conta = conta
    
    def get_conta(self):
        return self._conta
 
class Banco:
    def __init__(self):
        self._clientes = []
        self._contas = []
    
    def adicionar_cliente(self, cliente):
        self._clientes.append(cliente)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)
    
    def autenticar(self, cliente, conta, agencia):
        if cliente in self._clientes and conta in self._contas and conta.get_agencia() == agencia:
            return True
        else:
            return False
 
# Exemplo de uso
banco = Banco()
 
conta1 = ContaCorrente("001", "12345", 1000.0, 500.0)
conta2 = ContaPoupanca("001", "67890", 2000.0)
 
cliente1 = Cliente("João Henrique", 30, conta1)
cliente2 = Cliente("Maria Vitória", 25, conta2)
 
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)
 
# Autenticação do banco
cliente = cliente1
conta = cliente.get_conta()
agencia = conta.get_agencia()
 
if banco.autenticar(cliente, conta, agencia):
    valor_saque = 1000.0
    if conta.sacar(valor_saque):
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.")
    else:
        print("Saldo insuficiente para saque.")
else:
    print("Autenticação falhou.")