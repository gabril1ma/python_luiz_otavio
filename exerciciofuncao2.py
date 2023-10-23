# Estudos de funções

#def impoupar(func, *args):
#    return func(*args)

#print(impoupar(parouimpar, resultado))

#carros = ["nissan","ferrari"]

#def carro(valor):

#    def modelo(produto):

#        return f"O valor do {produto} é {valor}"
    
#    return modelo


#valor_nissan = carro(100000)
#valor_ferrari = carro(1000000)

#for i in ["nissan","ferrari","ferrari"]:
#    if i == "nissan":
#        print(valor_nissan(i))
#    if i == "ferrari":
#        print(valor_ferrari(i))


def operacoes(quantidade):
    def resolver(numero):
        return numero * quantidade
    return resolver

duplicar = operacoes(2)
triplicar = operacoes(3)
quadruplicar = operacoes(4)

print(duplicar(4))

def operar(quantidade,numero):
    
    if quantidade == 2:
        return numero * 2
    if quantidade == 3:
        return numero * 3
    if quantidade == 4:
        return numero * 4
    
print(operar(2,4))


        