def imprimir_par(lista_numeros):
    for i in lista_numeros:
        if int(i) % 2 == 0:
            print(i)
            



numeros = input("digite uma lista de num1eros: ").split(",")
print(numeros)
imprimir_par(numeros)