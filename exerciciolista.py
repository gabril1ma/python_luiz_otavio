#lista = ["gabriel", "david", "ghc"]

#indices = range(len(lista))

#for i in indices:
#   print(i, lista[i])


#or indice, nome in enumerate(lista):
 #   print(indice, nome)


itens = []
print("[i]nserir [a]pagar [l]istar")

escolha = input("Escolha uma opção: ")


while escolha in {"i", "a", "l"}:
    match escolha:

        case "i":
            item = input("Digite o item: ")
            itens.append(item)

        case "a":
            if len(itens) == 0:
                print("Lista vazia")
            for indice, nome in enumerate(itens):
                print(indice, nome)
            numero = int(input("Digite o indice do item que voce deseja apagar: "))
            itens.remove(itens[numero])

        case "l":
            for indice, nome in enumerate(itens):
                print(indice,nome)

    escolha = input("Escolha uma opção: ")
    print("[i]nserir [a]pagar [l]istar")


