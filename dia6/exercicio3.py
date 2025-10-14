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
    # Seu código aqui
    pass

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
# Notação Big O:
# Resultado: O(...)