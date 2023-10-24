#exercicio aula 169

def zipper(lista1,lista2):
    dic = dict(zip(lista1,lista2))
    return dic



teste1 = [1,2,3,4,5]
teste2 = ['a','b','c','d','e']


print(zipper(teste1,teste2))



numeros1 = [1,2,3,4,5]
numeros2 = [6,7,8,9,10,11]



# exercicio aula 171
for i, j in zip(numeros1,numeros2):
    print(i + j)



