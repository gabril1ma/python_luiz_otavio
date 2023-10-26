class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Vendedor(Pessoa):
    ...

c1 = Cliente("gabriel", "lima")
v1 = Vendedor("Ghc", "e silva")

print(c1.nome, c1.sobrenome)

c1.falar_nome_classe()


print(v1.nome, v1.sobrenome)

v1.falar_nome_classe()


class MinhaListagem(str):
    def upper(self):
        print("é o upper ntj")
        retorno = super().upper()
        print("Depois do upper")

        return retorno
    
texto = MinhaListagem("gabriel")
print(texto.upper())
    

class A:
    atributo_a = "A"

    def metodo(self):
        print(self.atributo_a)

class B(A):
    atributo_b = "B"

    def metodo(self):
        print(self.atributo_b)

class C(B):
    atributo_c = "C"

    def metodo(self):
        super().metodo() # vai puxar da classe exatamente acima dela 
        super(B, self).metodo() # vai puxar da classe acima da classe B
        print(self.atributo_c, self.atributo_b) # pode utilizar as variaveis das classes acima


class D(C,A): # ele puxa na ordem em que está inserido
    ...

print(D.mro())