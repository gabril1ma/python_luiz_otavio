lista = [[1,2,3,4,5,2,6,7],
         [1,2,3,4,5,6,7,3],
         [1,2,3,4,5,6,7,8]]

contagem = []

for i in lista:

    for j in i:
        if j not in contagem:
            contagem.append(j)
        
        else:
            print(j)
            contagem.clear()
            break
    
    if contagem == i:
        print(-1)


def repeticoes(lista):
    contagem = []
    retorno = []
    for i in lista:
        for j in i:
            if j not in contagem:
                contagem.append(j)
        
            else:
                contagem.clear()
                retorno.append(j)
                break
                
    
        if contagem == i:
            retorno.append(-1)
        
    return retorno

print(repeticoes(lista))

        
    