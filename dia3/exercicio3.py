# --- Nova Questão: Gerador de Sequência Fibonacci ---
#
# A sequência de Fibonacci é uma série de números onde cada número é a soma dos dois anteriores.
# A sequência geralmente começa com 0 e 1.
# Exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Crie uma função chamada `gerar_fibonacci(n)`.
# - A função deve receber um número inteiro `n` como argumento, que representa quantos termos da sequência você quer gerar.
# - A função deve retornar uma lista contendo os `n` primeiros números da sequência de Fibonacci.
#
# Casos especiais:
# - Se `n` for 0, deve retornar uma lista vazia `[]`.
# - Se `n` for 1, deve retornar `[0]`.
#
# Dica: Comece com uma lista como `[0, 1]`. Use um laço `while` ou `for` para continuar adicionando o próximo número (a soma dos dois últimos) à lista até que ela tenha o tamanho `n`.
#
# Exemplo de uso:
# print(gerar_fibonacci(10))
#
# A saída esperada seria: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]