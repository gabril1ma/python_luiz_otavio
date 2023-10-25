import json
print("comandos : listar, desfazer, refazer, sair")

comandos = ["listar", "desfazer", "refazer", "sair"]

def inserir_comando():
    comando = input("Digite o comando: ")
    return comando

comando = inserir_comando()

while comando not in comandos:
    print("Comando invalido")
    print("comandos : listar, desfazer, refazer, sair")
    inserir_comando()

lista_fazer = [] 
lista_desfazer = []

while comando in comandos:
    match comando:
        case "listar":
            print(lista_fazer)
            lista_fazer.append(input("Digite a tarefa: "))
            comando = inserir_comando()

        case "desfazer":
            if len(lista_fazer) == 0:
                print("nada a desfazer")
                comando = inserir_comando()
            
            else:
                lista_desfazer.append(lista_fazer.pop())
                print("tarefa desfeita")
                print(lista_fazer)
                comando = inserir_comando()

        case "refazer":
            if len(lista_desfazer) == 0:
                print("nada a refazer")
                comando = inserir_comando()
            
            else:
                lista_fazer.append(lista_desfazer.pop())
                print("tarefa refeita")
                print(lista_fazer)
                comando = inserir_comando()

        case "sair":
            with open("tarefas.json", "w") as a:
                json.dump(lista_fazer, a)
            break


        