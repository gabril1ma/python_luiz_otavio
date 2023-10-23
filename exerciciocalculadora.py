operadores = ['+', '-', '*', '/']


num1 = float(input("Digite um numero: "))
operador = input('Digite o operador: ')
num2 = float(input("Digite outro numero: "))
resultado = 0
final = 0
num3 = 0

if operador not in operadores:
    print("Operador inválido")

    
match operador:
    case '+':
        resultado = num1 + num2
    case "-":
        resultado = num1 - num2
    case "*":
        resultado = num1 * num2
    case "/":
        resultado = num1 / num2

print(num1, operador, num2, "=", resultado)

operador = input('Digite o operador: ')


while operador in operadores:
    num3 = float(input("Digite outro numero: "))
    match operador:
        case '+':
            final = resultado + num3
        case "-":
            final = resultado - num3
        case "*":
            final = resultado * num3
        case "/":
            final = resultado / num3

    print(resultado, operador, num3, "=", final)
    operador = input('Digite o operador: ')

print("fim")



