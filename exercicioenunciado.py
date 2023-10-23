# exercicio 1
numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero %2 != 0:
        print(f"O número {numero} é ímpar")
    else:
        print(f"O número {numero} é par")

else:
    print("O valor digitado não é um numero inteiro")


# exercicio 2

hora = float(input("Digite a hora atual: "))

if hora >= 0 and hora < 12:
    print("Bom dia")
elif hora >= 12 and hora < 18:
    print("boa tarde")

else: print("boa noite")

# exercicio 3

primeiro = input("Digite o seu primeiro nome: ")

if len(primeiro) <= 4:
    print("Seu nome é curto")
elif len(primeiro) > 4 and len(primeiro) <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")

