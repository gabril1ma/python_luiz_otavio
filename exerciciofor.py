import os
secreta = "gabriel"
acertadas = ""
tentativas = 0

while True:
    letra = input("Digite uma letra: ")

    if len(letra) > 1 or len(letra) < 1:
        print("Invalido")
        continue

    if letra in secreta:
        acertadas += letra

    formada = ""
    for letra_secreta in secreta:
        if letra_secreta in acertadas:
            formada += letra_secreta
        else:
            formada += "*"

    print(formada)
    tentativas += 1
    if formada == secreta:
        os.system("clear")
        print(f"A palavra era {secreta}")
        break


print(f"Parabens voce encontrou a palavra em {tentativas} tentativas")