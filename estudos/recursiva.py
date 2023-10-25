from functools import reduce

def fatorial(numero):
    
#    numeros = []
#    for i in range(numero):
#        numeros.append(i)
    
    numeros = [i for i in range(numero + 1) if i != 0]
    fator = reduce(lambda x, y: x * y, numeros)
    
    return fator


print((fatorial(4)))

