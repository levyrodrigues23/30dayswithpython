# --- Nova Questão: Verificador de Anagramas ---
#
# Anagramas são palavras ou frases formadas pela reorganização das letras de outra palavra ou frase.
# Por exemplo, "amor" e "roma" são anagramas. "listen" e "silent" também são.
#
# Crie uma função chamada `sao_anagramas(string1, string2)`.
# - A função deve receber duas strings.
# - Ela deve retornar `True` se as duas strings forem anagramas uma da outra, e `False` caso contrário.
# - Para um desafio adicional, faça a função ignorar espaços e diferenças entre maiúsculas e minúsculas.
#   Por exemplo, "I am Lord Voldemort" e "Tom Marvolo Riddle" devem ser considerados anagramas.
#
# Dica: Duas strings são anagramas se, após remover espaços, converter para a mesma caixa (maiúscula ou minúscula) e ordenar suas letras, elas se tornam idênticas. A função `sorted()` pode ser útil aqui.
#
# Exemplo de uso:
# print(sao_anagramas("listen", "silent"))  # Deve retornar True
# print(sao_anagramas("python", "java"))    # Deve retornar False

def sao_anagramas(string1, string2):
    string2_ao_contrario = string2[::-1]
    if string1 == string2_ao_contrario:
        return print(True)
    else:
        return print(False)
    
    
strings = input("digite duas palavras separadas em sequencia e eu direi se elas são anagramas: ").split()
sao_anagramas(strings[0], strings[1])
  

# atividade interessante, bem tranquila de realizar
    
    
    
    
    

    