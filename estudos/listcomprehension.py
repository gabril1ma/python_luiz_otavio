import pprint

def p(i):
    pprint.pprint(i, sort_dicts=False, width=40)

lista = []

for numero in range(1, 10):
    lista.append(numero)


lista = [numero for numero in range(10)]
print(lista)


lista = [numero % 2 == 0 for numero in range(100)]
print(lista)


lista = [numero for numero in range(100) if numero % 2 == 0]
print(lista)

lista = [numero for numero in range (100) if numero % 3 == 0 or numero % 5 == 0]
print(lista)


produtos = [
    {"nome": "p1", "preco": 50},
    {"nome": "p2", "preco": 13},
    {"nome": "p3", "preco": 20},
    {"nome": "p4", "preco": 10},
    {"nome": "p5", "preco": 100},
]

# Criando uma lista nova com uma operação aplicada em todos os elementos da lista
novos_produtos = [
    {**produto, "preco": produto["preco"] * 2}    
    for produto in produtos
]

# Criando uma lista nova com uma operação aplicada nos elementos que se encaixam na condição
new_products = [
    {**produto, "preco": produto["preco"] * 1.5}
    if produto["preco"] > 40 else {**produto}
    for produto in produtos
]

# Criando uma lista nova com um operação aplicada nos elementos que se encaixam na condição
# e que o resultado da operação esteja dentro da segunda condição

products = [
    {**produto, "preco": produto["preco"] * 1.2}
    if produto["preco"] > 40 else {**produto}
    for produto in produtos
    if (produto["preco"] * 1.2) < 100
]

# primeiro if utilizado para realizar o mapeamento dos elementos
# segundo if utilizado para filtrar o elementos que quero levar para a nova lista

print(*novos_produtos)
print(*new_products)

p(products)

valores = []

for x in range(3):
    for y in range(3):
        valores.append((x,y))

print(valores)

valores = [
    (x,y) for x in range(3) for y in range(3)
]
print(valores)

valores = [
    [letra for letra in "Gabriel"]  # criar 3 listas dentro da lista valores com todas as letras de gabriel
    for x in range(3)
]

print(valores)








