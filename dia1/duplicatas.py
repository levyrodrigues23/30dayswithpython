def calcular_duplicatas(lista):
    duplicatas = []
    valores_repetidos = [x for x in lista if lista.count(x) > 1]
    for valor in valores_repetidos:
        if valor not in duplicatas:
            duplicatas.append(valor)
    return duplicatas
    
    
    
  

usuario = input("digite uma lista de números separados por vírgula").split(",")
usuario = [item.strip() for item in usuario]
print(calcular_duplicatas(usuario))