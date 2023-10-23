lista = [
    {"nome" : "Gabriel", "idade" : 20},
    {"nome" : "David", "idade" : 19},
    {"nome" : "GHC", "idade" : 21},
]


def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item["nome"])
l2 = sorted(lista, key=lambda item: item["idade"])


exibir(l1)
exibir(l2)

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y
    soma(2,3)


    executa(soma, 2,3)

print(
    executa(lambda x, y: x + y, 2, 3), # mesma coisa da função soma criada acima

)

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica_exemplo = cria_multiplicador(2)

# mesma função da acima mas criada com lambda
duplica = executa(lambda m: lambda n: m * n, 2)

print(duplica(4))