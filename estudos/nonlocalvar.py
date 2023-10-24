def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final # para ser utilizada dentro da função inteira
        valor_final += valor_a_concatenar
        return valor_final
    return interna


a = concatenar("Salve, ")

print(a("Visitante desconhecido!"))