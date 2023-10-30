import contas
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.nome!r}, {self.idade!r}"
        return f"{class_name}({attrs})"
    
class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None
    
#    def get_conta(self):
#        return self.conta
    

if __name__ == "__main__":
    
    c1 = Cliente("gabriel", 20)
    c1.conta = contas.ContaCorrente(10, 20, 0, 0)

    print(c1)
    print(c1.conta)

    c2 = Cliente("Wellington", 42)
    c2.conta = contas.ContaPoupanca(40,69,49)
    print(c2)
    print(c2.conta)

    
