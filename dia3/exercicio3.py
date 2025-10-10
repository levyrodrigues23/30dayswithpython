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

lista_fibonacii = [0, 1]



""" def gerar_fibonacci(num: int):
    if num == 0:
        return []
    elif num == 1:
        return [0]
        
    for i in range(num):
        soma_valores = lista_fibonacii[i] + lista_fibonacii[i + 1]
        lista_fibonacii.append(soma_valores)
    
    return lista_fibonacii
    
    
print(gerar_fibonacci(100)) """

def gerar_fibonacci(n):
    # Trata os casos especiais primeiro
    if n <= 0:
        return []
    if n == 1:
        return [0]

    # Inicia a lista DENTRO da função para que seja sempre nova
    resultado = [0, 1]

    
    while len(resultado) < n:
        proximo = resultado[-1] + resultado[-2]
        resultado.append(proximo)       
        
        
    return resultado 
    
    
# COMOOOOOOOOOOOOOOO EU CONSEGUIIIIIIIIII, QUE INCRIVEL, EU NÃO SEI COMO MAS EU CONSEGUI, MOLEZAA
# deu bom, mas parece ter complexidade n + 2, que droga







try:
    numero_usuario = int(input("Quantos termos da sequência de Fibonacci você quer gerar? "))
    sequencia = gerar_fibonacci(numero_usuario)
    print(sequencia)
except ValueError:
    print("Por favor, digite um número inteiro válido.")