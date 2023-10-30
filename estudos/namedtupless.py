from collections import namedtuple

Carta = namedtuple('Carta', ['valor' , 'naipe'])

c1 = Carta("4", "Paus")

print(c1)

print(c1.valor)
print(c1[0])

print(c1.naipe)
print(c1[1])


# funciona do mesmo jeito que acima mas agora é uma classe
class Carta(namedtuple):
    valor: str = "VALOR"
    naipe: str = "NAIPE"

