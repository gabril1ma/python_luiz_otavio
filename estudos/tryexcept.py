
a = 0
b = 10

try:
    c = b / a

except ZeroDivisionError:
    print("Divisão por zero")
except NameError:
    print("variavel não definida")

# da pra colocar mais de uma excesão no mesmo except
except (IndexError, KeyError):
    print("Erro de indice ou chave")

except ValueError as erro:
    print(erro)

finally:
    print("Sempre executa")

# raise ValueError("levante o erro manualmente")


def deve_ser_int(n):
    if not isinstance(n, int):
        raise ValueError(f"{n} precisa ser inteiro")
    return True

def divide(n,d):
    deve_ser_int(n)
    deve_ser_int(d)
    return n / d

print(divide(2,"0"))