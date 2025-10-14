# --- Dia 4: Exercício 4 - Soma dos Dígitos ---
#
# Crie uma função chamada `soma_digitos(numero)` que recebe um número inteiro positivo.
# A função deve retornar a soma de todos os seus dígitos.
#
# Dica: Uma maneira de fazer isso é converter o número para uma string. Depois, você pode iterar sobre cada caractere da string, convertê-lo de volta para inteiro e somá-lo.
#
# Exemplo de uso:
# print(soma_digitos(1234))  # Deve retornar 10 (1+2+3+4)
# print(soma_digitos(987))   # Deve retornar 24 (9+8+7)


def soma_digitos(numero):
    soma = 0
    lista_pedaco = str(numero)

    for i in lista_pedaco:
        
        soma += int(i)
        
    return soma
        
        
        
print(soma_digitos(1234))

# trivial, essa é passada no concurso da prefeitura 
