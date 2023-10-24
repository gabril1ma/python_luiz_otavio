def soma(x):
    def resolver(y):
        return x + y
    return resolver

def multiplica(x):
    def resolver(y):
        return x * y
    return resolver


def criar_funcao(funcao, *args):
    return funcao(*args)

somar_por_cinco = soma(5)
multiplicar_por_dez = multiplica(10)

print(somar_por_cinco(10))
print(multiplicar_por_dez(15))
print(criar_funcao(multiplicar_por_dez, 20))
print(criar_funcao(somar_por_cinco, 30))

