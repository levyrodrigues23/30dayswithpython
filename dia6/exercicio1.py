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
    soma = 0
    for i in numeros:
        soma += int(i)
    
    return soma

lista = input("digite uma lista de números separados por virgula").split(",")
print(soma_lista(lista))





# --- Análise de Complexidade ---
#
# Seja 'n' o número de elementos na lista `numeros`.
#
# Contagem de Operações:
# 1. `soma = 0`: ... (quantas operações?) - o custo da linha vale 1 e o custo da operação vale 1

# 2. `for numero in numeros`: O laço executa ... vezes. o custo da linha vale 2, porque tem o for e tem a verificação se i está em numeros, e o custo da operação vale n
# 3. `soma = soma + numero`: Dentro do laço, temos ... operações (adição, atribuição). Isso acontece ... vezes. - custo vale 2 e o da operação vale n
# 4. `return soma`: ... (quantas operações?) custo 1 e operação 1
#
# Equação T(n):
# T(n) = (operações fora do laço) + (operações dentro do laço * n)
# T(n) = fazendo a multiplicaççao de cada e depois a soma, fica 1c + 2cn + 2cn + 1c, e ent depois a formula fica 
# T(n) = 4cn + 2c
# Notação Big O:
# Resultado: O(n)