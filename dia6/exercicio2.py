# --- Dia 6: Exercício 2 - Análise Detalhada (Quadrática) ---
#
# Objetivo: Encontrar e retornar o primeiro par de elementos duplicados em uma lista.
#
# --- Tarefa ---
# 1. Escreva uma função `encontrar_primeira_duplicata(lista)` que usa laços aninhados (um `for` dentro de outro `for`) para encontrar o primeiro item que aparece mais de uma vez.
#    - Se encontrar uma duplicata, a função deve retornar esse item.
#    - Se não houver duplicatas, deve retornar `None`.
#
# 2. Faça a análise de complexidade (pior caso) da sua função:
#    - **Pior Caso:** A lista não tem duplicatas.
#    - **Contagem de Operações:** Descreva as operações e conte-as. Preste atenção em como os laços aninhados se comportam.
#    - **Equação T(n):** Escreva a função T(n) para o pior caso.
#    - **Notação Big O:** Simplifique a equação T(n).
#
# --- Escreva seu código e análise abaixo ---

def encontrar_primeira_duplicata(lista):
    # Seu código aqui
    pass

# --- Análise de Complexidade (Pior Caso) ---
#
# Seja 'n' o número de elementos na lista.
#
# Contagem de Operações:
# 1. Laço externo (`for i in range(n)`): Executa n vezes.
# 2. Laço interno (`for j in range(n)`): Para CADA execução do laço externo, este executa n vezes.
# 3. `if i != j and lista[i] == lista[j]`: Dentro do laço interno, temos ... operações (comparações, acessos).
#
# Equação T(n):
# O número total de vezes que o `if` executa é aproximadamente n * n.
# T(n) ≈ n * n * (operações do if) + (outras operações menores)
# T(n) = ...
#
# Notação Big O:
# Resultado: O(...)