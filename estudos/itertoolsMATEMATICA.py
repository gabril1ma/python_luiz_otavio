from itertools import combinations, permutations, product, groupby
from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep="\n")
    print()

pessoas = ["Gabriel", "David", "João", "Maria", "José", "Ana"]
camisetas = [["galo", "barça", "milan", "city"],
             ["p", "m", "g", "gg"],
             ["masculina", "feminino"],
             ["azul", "vermelho", "amarelo", "verde", "preto", "branco"],

]

print_iter(combinations(pessoas, 2)) # agrupa todos os itens da lista em combinações unicas
print_iter(permutations(pessoas, 2)) # agrupa todos os itens da lista em combinações que se repetem com as posições

print_iter(product(*camisetas)) # desempacota todos os itens da lista dentro das listas e os agrupa em todas as combinações possiveis


alunos = [
    {"nome": "Gabriel", "nota": 10},
    {"nome": "David", "nota": 4},
    {"nome": "João", "nota": 3},
    {"nome": "Maria", "nota": 10},
    {"nome": "José", "nota": 4},
    {"nome": "Ana", "nota": 10},

]

def ordena(aluno):
    return aluno["nota"]

alunos.sort(key=lambda item: item["nota"]) # para mudar a lista original
agrupados = sorted(alunos, key=lambda item: item["nota"]) # para criar uma nova lista com os dados ordenados
agrupados = sorted(alunos, key=ordena) # mesmo codigo acima mas usando função

grupos = groupby(agrupados, key=lambda item: item["nota"])
grupos = groupby(agrupados, key=ordena) # mesmo codigo acima mas utilizando função


for key, grupo in grupos:
    print(key)
    for aluno in grupo:
        print(aluno)

# map recebe uma função e depois o elemento iteravel

print(list(map(
    lambda i: i["nota"] * 2,
    alunos
)))
# filtragem utilizando list comprehension
novas_notas = [
    n for n in alunos
    if n["nota"] > 5
]

print(novas_notas)

# filtragem utilizando filter com uma lambda
novas_notas = list(filter(
    lambda n: n['nota'] > 3,
    alunos
))

print(novas_notas)

def filtrar_nota(nota):
    return nota["nota"] > 3

# filtragem utilizando filter com uma função
novas_notas = list(filter(filtrar_nota, alunos))

print(novas_notas)


produtos = [
    {"nome": "p1", "preco": 13},
    {"nome": "p2", "preco": 55.55},
    {"nome": "p3", "preco": 5.59},
    {"nome": "p4", "preco": 22},
    {"nome": "p5", "preco": 81.23},
    {"nome": "p6", "preco": 5.59},
    {"nome": "p7", "preco": 10},
    {"nome": "p8", "preco": 10.90},
    {"nome": "p9", "preco": 89.99},
    {"nome": "p10", "preco": 12.99},
]

def funcao_reduce(acumulador, produto):
    print("acumulador", acumulador)
    print("produto", produto)
    print()
    return acumulador + produto["preco"]

total = reduce(
    funcao_reduce,
    produtos,
    0
)

# utilizando lambda

total = reduce(
    lambda ac, p: ac + p["preco"],
    produtos,
    0
)

