def calcular_frequencia(itens):
    dicionario_frequencia = {}
    for i in itens:
        if i in dicionario_frequencia:
            dicionario_frequencia[i] += 1
        else:
            dicionario_frequencia[i] = 1
            
    return dicionario_frequencia
            

lista_itens = input("digite uma lista de números ou palavras separados por vírgula").split(",")
print(calcular_frequencia(lista_itens))


# --- Nova Questão: Contador de Frequência ---
#
# Escreva uma função chamada `contar_frequencia` que recebe uma lista de itens (podem ser números ou strings).
# A função deve retornar um dicionário onde as chaves são os itens da lista e os valores são o número de vezes que cada item aparece.
#
# Exemplo: Se a lista for `['maçã', 'banana', 'maçã', 'laranja', 'banana', 'maçã']`
# A função deve retornar: `{'maçã': 3, 'banana': 2, 'laranja': 1}`
#
# Dica: Crie um dicionário vazio. Percorra a lista item por item.
# Para cada item, verifique se ele já existe como uma chave no seu dicionário.
# Se existir, incremente o valor associado a essa chave.
# Se não existir, adicione o item ao dicionário com o valor 1.