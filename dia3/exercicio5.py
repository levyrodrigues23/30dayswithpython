# --- Nova Questão: Encontrar Palavras Longas ---
#
# Escreva uma função chamada `encontrar_palavras_longas` que recebe dois argumentos:
# 1. Uma string `frase`.
# 2. Um número inteiro `n`.
#
# A função deve retornar uma lista contendo todas as palavras da `frase` que têm um comprimento (número de letras) maior que `n`.
#
# Dica: O método de string `.split()` pode ser usado para transformar a frase em uma lista de palavras. Depois, você pode percorrer essa lista e verificar o comprimento de cada palavra com `len()`.
#
# Exemplo de uso:
# texto = "O rápido cão marrom salta sobre o cão preguiçoso"
# tamanho_minimo = 4
# print(encontrar_palavras_longas(texto, tamanho_minimo))
#
# A saída esperada seria: ['rápido', 'marrom', 'salta', 'sobre', 'preguiçoso']

lista_maior = []
def encontrar_palavras_longas(frase, num):
    
    for i in frase:
        lista_maior.append(i)
        
    palavras_maiores = [i for i in lista_maior if len(i) > num]
    
    return print(palavras_maiores)
   

 
frase = input("campo para voce digitar sua frase: ").split()



num = int(input("tamanho minimo: ")) 
encontrar_palavras_longas(frase, num)


# atividade tranquilinha, demorei um tempinho porque tentei deixar bonito, mas o básico ja serve, muito boa atividade

