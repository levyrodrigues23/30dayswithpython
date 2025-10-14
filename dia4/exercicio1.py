# --- Dia 4: Exercício 1 - Contador de Vogais ---
#
# Crie uma função chamada `contar_vogais(texto)` que recebe uma string e retorna o número de vogais (a, e, i, o, u) presentes nela.
# A função deve ser "case-insensitive", ou seja, deve contar tanto 'a' quanto 'A'.
#
# Dica: Você pode criar uma string ou lista com todas as vogais e verificar se cada caractere do texto (convertido para minúsculo) está nela.
#
# Exemplo de uso:
# print(contar_vogais("Ola, Mundo!"))  # Deve retornar 4
# print(contar_vogais("Python e Incrivel")) # Deve retornar 5


def contar_vogais(texto):
    vogais = []
    lista_vogais = list(texto)
    for i in lista_vogais:
        if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
            vogais.append(i)
            
            
            
    return len(vogais)
        
    
    

    
print(contar_vogais("Ola, Mundo!"))  
print(contar_vogais("Python e Incrivel"))

# trivial