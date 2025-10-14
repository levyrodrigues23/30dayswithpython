# --- Dia 6: Exercício 1 - Análise Detalhada (Linear) ---
#
# Objetivo: Calcular a soma de todos os elementos em uma lista de números.
#
# --- Tarefa ---
# 1. Escreva uma função `soma_lista(numeros)` que recebe uma lista de números e retorna a soma deles.
#    - Não use a função pronta `sum()`. Use um laço `for`.
#
# 2. Faça a análise de complexidade da sua função:
#    - **Contagem de Operações:** Descreva cada operação (atribuição, comparação, acesso, etc.) e conte quantas vezes ela ocorre.
#    - **Equação T(n):** Escreva a função T(n) que representa o número total de operações, onde 'n' é o número de elementos na lista.
#    - **Notação Big O:** Simplifique a equação T(n) para encontrar a complexidade em notação Big O.
#
# --- Escreva seu código e análise abaixo ---

def soma_lista(numeros):
    # Seu código aqui
    pass

# --- Análise de Complexidade ---
#
# Seja 'n' o número de elementos na lista `numeros`.
#
# Contagem de Operações:
# 1. `soma = 0`: ... (quantas operações?)
# 2. `for numero in numeros`: O laço executa ... vezes.
# 3. `soma = soma + numero`: Dentro do laço, temos ... operações (adição, atribuição). Isso acontece ... vezes.
# 4. `return soma`: ... (quantas operações?)
#
# Equação T(n):
# T(n) = (operações fora do laço) + (operações dentro do laço * n)
# T(n) = ...
#
# Notação Big O:
# Resultado: O(...)