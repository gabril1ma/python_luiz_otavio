#frase = "AHAHHAHAHAHAHA, heheheheheheheh"

#frases_cruas = frase.split(",")

#lista_frases = []

#for i, frase in enumerate(frases_cruas):
#    lista_frases.append(frases_cruas[i].strip())

#frases_unidas = "-".join(lista_frases)
#print(frases_unidas)


# primeiro digito

multiplicadores = []
multiplicadores2 = []
cpf = "746.824.890-70"

cpf = cpf.replace(".", "")
cpf = cpf.replace("-", "")

separado = []
resultado = []

for i in cpf:
    separado.append(int(i))

print(separado)

for i in range (10, 1, -1):
    multiplicadores.append(i)

for i in range (11, 1, -1):
    multiplicadores2.append(i)

indices = range(len(multiplicadores))
indices2 = range(len(multiplicadores2))


for i in indices:
    resultado.append(multiplicadores[i] * separado[i])

soma = sum(resultado)

print(multiplicadores)
print(resultado)
print(soma)

digito_temp = (soma * 10) % 11

if digito_temp > 9:
    digito = 0
else:
    digito = digito_temp

print(digito)
final = separado[:9] + [digito]

# segundo digito

resultado2 = []

for i in indices2:
    resultado2.append(multiplicadores2[i] * separado[i])

print(resultado2)

soma = sum(resultado2)

print(soma)

digito_temp = (soma * 10)  % 11

if digito_temp > 9:

    digito = 0
else:
    digito = digito_temp

print(digito)

final = final + [digito]

print(separado)
print(final)

if final == separado:
    print("Parabens, seu cpf é valido e meu programa funcionou")
else:
    print("infelizmente seu cpf é invalido e meu programa continua funcionando")




