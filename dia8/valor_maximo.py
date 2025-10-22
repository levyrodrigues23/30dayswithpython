def buscar_valor_maximo(lista):
    maximo = int(lista[0])
    for i in lista[1:]:
        numero_atual = int(i)
        if numero_atual > maximo:
            maximo = numero_atual
    return maximo



# Diga ao split para usar a vírgula como separador
lista_usuario = list(input("digite uma lista de numeros e eu retornarei o valor maximo desta lista: ").split(','))
print(buscar_valor_maximo(lista_usuario))
