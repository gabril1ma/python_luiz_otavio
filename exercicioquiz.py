'''
pessoa = {"macho" : 4}

chave = "nome"

pessoa[chave] = "Gabriel"

print(pessoa)

del pessoa["nome"]

print(pessoa)

print(pessoa["macho"])

if pessoa.get("nome", "valor a ser inserido") is None:
    print("Não existe")
else: 
    print("EXIISTE")

print(list(pessoa.keys()))
print(list(pessoa.values()))
print(list(pessoa.items()))

for key, value in pessoa.items():
    print(key, value)

pessoa.setdefault("calica", "aiii") # colocar um valor padrão para uma chave caso ela não exista


pessoa2 = pessoa.copy() # para copiar todos os dados imutaveis NÂO COPIA LISTAS
linka os dois dicionarios para a mesma lista então se mudar um muda o outro

import copy

pessoa3 = copy.deepcopy(pessoa) # para copiar todos os dados inclusive listas

pessoa.get("valor", 0) + 1 # caso o valor não exista ele inicia com zero e soma 1

nome = pessoa.pop("nome") # remove o item e retorna o valor
ultima_chave = p1.popitem() # remove o ultimo item e retorna o valor

pessoa.update({
    "nome" : "Gabriel"
    "idade" : 20
}) # adiciona um item ao dicionario

pessoa.update(nome= "novo valor", idade= 21)

tupla = (("nome", "idade"), (idade, 22))
lista = [["nome", "idade"], [idade, 22]]

pessoa.update(tupla)
pessoa.update(lista)
'''

import os

perguntas = [
    {
        "Pergunta" : "Quantos integrantes tem o grupo?",
        "Opcoes": ["2","5","7","4","6"],
        "Resposta": "6",
    },

    {
        "Pergunta": "Quantos estão desempregados?",
        "Opcoes": ["5","4","3","2","1"],
        "Resposta": "1",
    },
    
    {
        "Pergunta": "Quantos ja tiraram carteira",
        "Opcoes": ["1", "2", "3", "4", "5"],
        "Resposta": "2"
    },
]

acertadas = 0

for i in perguntas:
    print(f'{i["Pergunta"]}?\n')
    print("Opções:")
    for indice, opcao in enumerate(i["Opcoes"]):
        print(f"{indice}) {opcao}")
    resposta_usuario = input("Digite sua resposta: ")

    if i["Resposta"] == i["Opcoes"][int(resposta_usuario)]:
        print("Acertou")
        acertadas += 1
        print(f'A sua pontuação é de: {acertadas}')

    else: 
        print("Errou")
        print(f'A sua pontuação é de: {acertadas}')

os.system("clear")
print(f'O jogo acabou! Voce acertou {acertadas} em {len(perguntas)}')





