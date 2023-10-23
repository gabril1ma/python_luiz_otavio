lista_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
]

resposta = 0

for i in lista_inteiros:
    print(i)

def duplicadas(lista_inteiros):
    repeticoes = []
       
            
    
repeticoes = []
indice = 0

for lista in lista_inteiros:

    for i in lista_inteiros[indice]:
        if repeticoes.count(i) == 0:
            repeticoes.append(i)
            
    indice += 1
    

print(repeticoes)