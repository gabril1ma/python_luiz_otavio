class Pessoa:
    def __init__(self, nome, sobrenome):

        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa("gabriel", "Lima")

print(p1.nome)
print(p1.sobrenome)



class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando vrummmvrummm")
    
    
    def freiar(self, velocidade):
        return f"{self.marca} {self.modelo} freando a {velocidade}km/h"

    def executar(self, *args):
        return self.freiar(*args)


ferrari = Carro("Ferrari", "F40", 2017)
lamborghini = Carro("Lamborghini", "Aventador", 2018)

ferrari.acelerar()

print(lamborghini.executar("MUITOOOOO RAPIDOOOOOO"))

class Dev:
    ano_atual = 2023
    def __init__(self, nome,idade, programando=False):
        self.nome = nome
        self.idade = idade
        self.programando = programando

    def programar(self):
        if self.programando:
            print(f"{self.nome} já está programando")
            return
        self.programando = True
        print(f"{self.nome} começou a programar {self.programando}")
    
    def ano_nascimento(self):
        return Dev.ano_atual - self.idade
    
    @classmethod  # pode ser utilizado para definir caracteristicas sem ter que passar o parametro
    # não é possivel usar os self dentro dele 
    def criar_programando(cls, nome, idade):
        return cls(nome, idade, programando=True)


gabriel  = Dev("Gabriel",20)
david = Dev("David",19, programando=True)

gabriel.programar()
david.programar()

print(gabriel.ano_nascimento())

print(vars(gabriel))

dados = {"nome":"calica", "idade":20, "programando":True}

calica = Dev(**dados)

print(calica.idade)

ghc = Dev.criar_programando("ghc", 19)

print(ghc.programando)
