# --- Dia 6: Exercício 3 - Análise de Múltiplos Laços (Linear) ---
#
# Objetivo: Calcular a média de uma lista e contar quantos números estão acima dela.
#
# --- Tarefa ---
# 1. Escreva uma função `contar_acima_da_media(numeros)`.
#    - Primeiro, calcule a soma de todos os números (use um laço `for`).
#    - Depois, calcule a média.
#    - Finalmente, use um SEGUNDO laço `for` para contar quantos números na lista são maiores que a média.
#
# 2. Faça a análise de complexidade da sua função:
#    - **Contagem de Operações:** Conte as operações para cada parte (primeiro laço, cálculo da média, segundo laço).
#    - **Equação T(n):** Some todas as operações para obter a equação T(n). Você terá dois termos com 'n'.
#    - **Notação Big O:** Simplifique a equação. O que acontece quando você tem `c1*n + c2*n`?
#
# --- Escreva seu código e análise abaixo ---

def contar_acima_da_media(numeros):
    soma = 0
    for numero in numeros:
        soma += numero
        
    media = soma / len(numeros)
    
    maiores_numeros = [x for x in numeros if x > media]
    print(media)
    return len(maiores_numeros)

numeros = [1,2,3,4,5,6,7,8,9]
print(contar_acima_da_media(numeros))
    
    
    

# --- Análise de Complexidade ---
#
# Seja 'n' o número de elementos na lista.
#
# Contagem de Operações:
# - Parte 1: Primeiro laço (soma)
#   - T₁(n) = ... (análise similar ao exercício 1)
# - Parte 2: Cálculo da média
#   - ... (quantas operações?)
# - Parte 3: Segundo laço (contagem)
#   - T₂(n) = ... (análise similar ao laço de soma)
#
# Equação T(n):
# T(n) = T₁(n) + (operações da média) + T₂(n)
# T(n) = (c₁*n + k₁) + k₂ + (c₂*n + k₃)
# T(n) = ...
#
# fazendo a contagem do custo de cada linha e depois o custo da operação de cada linha, posso chegar no seguinte quadro: CUSTO/ #OPERAÇÃO
# 1 linha: 1c/1
# 2 linha: 2c/n
# 3 linha: 2c/n
# 4 linha: 2c/1 - eu não contei o len, meu professor disse que não valia pois não está em memoria
# 5 linha: 4c/n
# 6 linha: 1c/1
# 7 linha: 1c/1
 # ai depois eu multiplico cada, posso chegar aproximadamente em um resultado equivalente a 1c + 2cn + 2cn + 2c + 4cn + 1c + 1c = 8cn + 3c


# Notação Big O:
# Resultado: O(n)