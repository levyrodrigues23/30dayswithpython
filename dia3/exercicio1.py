# --- Nova Questão: Filtrar Números Primos ---
#
# O objetivo é criar uma função que filtra apenas os números primos de uma lista.
#
# 1. Crie uma função chamada `eh_primo(numero)`.
#    - Esta função deve receber um número inteiro e retornar `True` se ele for primo, e `False` caso contrário.
#    - Lembre-se: um número primo é maior que 1 e só é divisível por 1 e por ele mesmo.
#    - Números como 0, 1 e números negativos não são primos.
#    - Dica: Para verificar se `numero` é primo, você pode tentar dividi-lo por todos os números de 2 até `numero - 1`. Se alguma dessas divisões tiver resto 0, ele não é primo.
#
# 2. Crie uma segunda função chamada `filtrar_primos(lista_de_numeros)`.
#    - Esta função deve receber uma lista de números inteiros.
#    - Usando a sua função `eh_primo`, ela deve criar e retornar uma nova lista contendo apenas os números que são primos.
#
# Exemplo de uso:
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15]
# print(filtrar_primos(lista))
#
# A saída esperada seria: [2, 3, 5, 7, 11, 13]

lista_primos = []


def eh_primo(numero_inteiro):
    if numero_inteiro <= 1:
        return False
    for i in range(2, numero_inteiro):
        if numero_inteiro % i == 0:
            return False
    return True
    
    
def filtrar_primos(lista_numeros):
    return print([i for i in lista_numeros if eh_primo(i)])

usuario = input("digite valores separados por virgula").split(",")
lista = [int(x) for x in usuario]
filtrar_primos(lista)
            
        
    

    
