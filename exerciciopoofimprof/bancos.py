import contas
import pessoas
class Banco:

    def __init__(self, 
                 agencias = [],
                 clientes = [pessoas.Pessoa],
                 contas = [contas.Conta]):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.lista_contas = contas or []
#        self.agencias.append(contas.Conta.agencia)
#        self.clientes.append(pessoas.Cliente.nome)
#        self.lista_contas.append(contas.Conta.conta)

    def checa_conta(self, conta):
        if conta in self.lista_contas:
            return True
        return False
    
    def checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False
    
    def checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
        
    def autenticar(self, cliente, conta):
        return self.checa_agencia(conta) and \
              self.checa_cliente(cliente) and \
              self.checa_conta(conta) and \
              True if cliente.conta == conta else False
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f"{self.agencias!r}, {self.clientes!r}, {self.lista_contas!r}"
        return f"{class_name}({attrs})"
        

if __name__ == "__main__":
    c1 = pessoas.Cliente("gabriel", 20)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1

    c2 = pessoas.Cliente("Wellington", 42)
    cp1 = contas.ContaPoupanca(333, 444, 0)
    c2.conta = cp1

    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.lista_contas.extend([cc1, cp1])
    banco.agencias.extend([111, 333])



    if banco.autenticar(c1, cc1):
        print("Opções: [1] Sacar [2] Depositar [3] Sair")
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                valor = float(input("Digite o valor do saque: "))
                cc1.sacar(valor)
            case "2":
                valor = float(input("Digite o valor do deposito: "))
                cc1.depositar(valor)
            case "3":
                print("Saindo")
    
    else:
        print("Cliente não autenticado")