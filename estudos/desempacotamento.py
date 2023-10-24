pessoa = {
    "Nome": "gabriel",
    "sobrenome": "Lima",
}

dados_pessoa = {
    "bom no cs": True,
    "idade": 20,
}

(a1, a2) = pessoa.items()

(b1, b2), (c1, c2) = pessoa.items()

print(a2)
print(b1)

for key, value in pessoa.items():
    print(key, value)


pessoa_completo = {**pessoa, **dados_pessoa, "sabe muito": True}
print(pessoa_completo)


def argumentos_nomeados(*args, **kwargs):
    print("nome", args)

    for key, value in kwargs.items():
        print(key, value)


argumentos_nomeados("gabriel", "lima")

argumentos_nomeados(nome="david", sobrenome="ferreira")