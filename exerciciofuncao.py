def multiplicar(*args):

    x =1 

    for i in args:
        x *= i
    
    return x

resultado = multiplicar(4,7,1,2,5)

print(resultado)

def parouimpar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "impar"


print(parouimpar(1))









