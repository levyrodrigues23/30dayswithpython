# --- Dia 4: Exercício 5 - Filtrar Palavras por Letra Inicial ---
#
# Crie uma função chamada `filtrar_por_letra(palavras, letra)` que recebe dois argumentos:
# 1. Uma lista de palavras (strings).
# 2. Uma letra (string de um caractere).
#
# A função deve retornar uma nova lista contendo apenas as palavras da lista original que começam com a `letra` fornecida. A verificação deve ser "case-insensitive".
#
# Dica: Use o método de string `.startswith()` ou verifique o primeiro caractere da palavra (`palavra[0]`). Lembre-se de usar `.lower()` ou `.upper()` para ignorar a diferença entre maiúsculas e minúsculas.
#
# Exemplo de uso:
# lista_de_frutas = ["Abacate", "Banana", "Maçã", "Amora", "Melancia"]
# print(filtrar_por_letra(lista_de_frutas, 'a'))
#
# A saída esperada seria: ['Abacate', 'Amora']