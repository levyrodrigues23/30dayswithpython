# --- Dia 6: Exercício 2 - Análise com Prova de Corretude ---
#
# Objetivo: Implementar uma busca linear e provar sua corretude.
#
# --- Tarefa ---
# 1. Escreva uma função `busca_linear(lista, item_procurado)` que recebe uma lista e um item.
#    - A função deve percorrer a lista e retornar `True` se encontrar o item, e `False` caso contrário.
#
# 2. Faça a análise de complexidade (pior caso) da sua função.
#    - Pior caso: O item não está na lista ou é o último elemento.
#
# 3. Faça a prova de corretude da sua função usando uma invariável de laço.
#
# --- Escreva seu código e análise abaixo ---

def busca_linear(lista, item_procurado):
    for item in lista:
        if item == item_procurado:
            return True
    return False

# --- Análise de Complexidade (Pior Caso) ---
#
# Seja 'n' o número de elementos na lista e 'c' o custo de uma operação.
#
# Contagem de Operações:
# 1. `for item in lista`: O laço executa ... vezes no pior caso. - n + 1
# 2. `if item == item_procurado`: Dentro do laço, temos ... operações (comparação). Isso acontece ... vezes. n + 1
# 3. `return True`: No pior caso, esta linha nunca executa 
# 4. `return False`: Executa 1 vez, após o laço. 
#
# Equação T(n):
# T(n) = (custo do laço * n) + (custo do retorno final)
# T(n) = (2c * n + 1) + (2c + n + 1) + 1c + 1c = 2cn + 1 + 2cn + 1 + 2c = 4cn + 4c 
#
# Notação Big O:
# Resultado: O(n)

# --- Prova de Corretude ---
#
# Para provar que o algoritmo está correto, usamos uma Invariável de Laço.
# Vamos reescrever o código usando um índice para facilitar a prova:
#
# def busca_linear(lista, item_procurado):
#     for i in range(len(lista)):
#         if lista[i] == item_procurado:
#             return True
#     return False
#
# **Invariável de Laço:**
# Defina uma propriedade que seja verdadeira no início de cada iteração do laço `for`.
# Invariável: "No início de cada iteração `i` do laço, o sub-array `lista[0...i-1]` não contém o `item_procurado`."
#
# **Prova:**
#
# 1. **Inicialização:**
#    - Antes da primeira iteração (quando `i = 0`), a invariável é verdadeira? 
#    - Explicação: (Pense no sub-array `lista[0...-1]`. O que ele representa?)
#
# 2. **Manutenção:**
#    - Assuma que a invariável é verdadeira no início de uma iteração `i`. Precisamos mostrar que ela será verdadeira no início da próxima iteração, `i+1`.
#    - Explicação: (Se a invariável é verdadeira, sabemos que o item não está em `lista[0...i-1]`. O código então verifica `lista[i]`. Se `lista[i]` não for o item, o que podemos dizer sobre o sub-array `lista[0...i]`? Como isso garante a invariável para a iteração `i+1`?)
#
# 3. **Término:**
#    - O laço termina por duas razões. Analise ambas:
#      a) O laço termina porque `lista[i] == item_procurado` e a função retorna `True`. O algoritmo está correto neste caso?
#         - Explicação:
#      b) O laço termina porque `i` percorreu toda a lista (chegou a `len(lista)`). A função então retorna `False`. O que a invariável nos diz neste ponto? O algoritmo está correto?
#         - Explicação: (No término, `i = n`. A invariável nos diz que o sub-array `lista[0...n-1]` não contém o item. O que isso significa?)