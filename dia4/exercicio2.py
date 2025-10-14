# --- Dia 4: Exercício 2 - Lista de Quadrados ---
#
# Crie uma função chamada `lista_quadrados(n)` que recebe um número inteiro positivo `n`.
# A função deve retornar uma lista com os quadrados dos números de 1 até `n`.
#
# Dica: Use um laço `for` com `range()` ou uma list comprehension.
#
# Exemplo de uso:
# print(lista_quadrados(5))
#
# A saída esperada seria: [1, 4, 9, 16, 25]

quadrados = []

def lista_quadrados(n):
    for i in range(1, n + 1):
        quadrado = i ** 2
        quadrados.append(quadrado)
    
    return quadrados
    
print(lista_quadrados(5))

# tranquila, terminei rapidinho