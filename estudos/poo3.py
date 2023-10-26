
# relação entre classes

class Piloto:
    def __init__(self, nome):
        self.nome = nome
        self._aviao = None

    @property
    def aviao(self):
        return self._aviao
    
    @aviao.setter
    def aviao(self, aviao):
        self._aviao = aviao



boeing = Piloto("Boeing")
print(boeing.aviao)
boeing.aviao = "Boeing 747"
print(boeing.aviao)

class VeiculoDeVoo:
    def __init__(self, modelo):
        self.modelo = modelo

    def voar(self):
        return f"{self.modelo} está voando"
    
aviao = VeiculoDeVoo("f50")
veiculo = aviao

print((veiculo.voar()))

# agregação entre classes

class Estoque:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.quantidade for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        self._produtos.extend(produtos) # extend funciona igual ao for de baixo
        for i in produtos:
            self._produtos.append(i)
    
    def listar_estoque(self):
        for produto in self._produtos:
            print(produto.nome, produto.quantidade)


class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade


estoque = Estoque()
 
p1, p2, p3 = Produto("trento", 20),Produto("coca", 40),Produto("salgadinho", 50)

estoque.inserir_produtos(p1,p2,p3)

estoque.listar_estoque()

print(estoque.total())


# composição entre classes

class cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for i in self.enderecos:
            print(i.rua, i.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


c1 = cliente("Gabriel")

c1.inserir_endereco("vista alegre", 55)
c1.inserir_endereco("alberto cintra", 161)

print(c1.enderecos[0].rua)
print(c1.enderecos[1].rua)

c1.listar_enderecos()

