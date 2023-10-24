carro  = {
    "marca": "uno",
    "ano": 2010,
    "preco": 20000.00
}


dc = {
    key: value.upper()
    if isinstance(value, str) else value
    # if isinstance(value, (int, float)) value * 2 else value
    # para mais de um valor botar dentro de uma tupla
    for key, value in carro.items()
}

dc = {
    key: value.upper()
    if isinstance(value, str) else value
    # if isinstance(value, (int, float)) value * 2 else value
    # para mais de um valor botar dentro de uma tupla
    for key, value in carro.items()
    if key == "marca" # para colocar apenas a chave marca
    # if key != "marca" # para retirar a chave marca e manter as outras 
}

#print(dc)


lista = [
    ("gabriel", "lima"),
    ("david", "ferreira"),
    ("joao", "silva"),
]

dicionario = {
    key: value
    for key, value in lista
}

dict(lista) # mesma coisa do codigo acima para transformar lista em dicionario


#print(dicionario)



teste = [
    "gabriel", 2, 4.5, False, [90,3,4], ("gabriel", "lima"), (4,7), {3,5},
    {"status": "online e operante"},
]

for i in teste:

    if isinstance(i, list):
        print(i, isinstance(i, list))

    if isinstance(i, str):
        print(i, isinstance(i, str))

    if isinstance(i, (int, float)):
        print(i, i * 2)
    
    print(i, isinstance(i, int))