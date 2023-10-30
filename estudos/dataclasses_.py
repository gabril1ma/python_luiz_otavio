from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    idade: int

    def __post_init__(self):
        self.idade_nome = f"{self.idade} {self.nome}"


    def nome_idade(self):
        return f"{self.nome} tem {self.idade} anos"
    
    
    

p1 = Pessoa("gabriel", 20)
print(p1)

print(p1.nome_idade())

print(p1.idade_nome)

print(asdict(p1))
