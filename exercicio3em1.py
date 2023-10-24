import copy

produtos = [
    {"nome": "calabresa", "preco": 50},
    {"nome": "tangerino", "preco": 13},
    {"nome": "rito cadilaco", "preco": 20},
    {"nome": "samsungo", "preco": 10},
    {"nome": "iphono", "preco": 100},
]

novos_produtos = copy.deepcopy(produtos)

for i in novos_produtos:
    i["preco"] = i["preco"] * 1.1


produtos_ordenados_por_nome = copy.deepcopy(produtos)

produtos_ordenados_por_nome = sorted(produtos, key=lambda i: i["nome"])

print(produtos_ordenados_por_nome)
    

produtos_ordenados_por_preco = copy.deepcopy(produtos)

produtos_ordenados_por_preco = sorted(produtos, key=lambda i: i["preco"])

print(produtos_ordenados_por_preco)
