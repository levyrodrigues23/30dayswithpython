# --- Dia 4: Exercício 3 - Inverter Dicionário ---
#
# Crie uma função chamada `inverter_dicionario(d)` que recebe um dicionário.
# A função deve retornar um novo dicionário onde as chaves originais viram valores e os valores originais viram chaves.
#
# Assuma que todos os valores no dicionário de entrada são únicos e podem ser usados como chaves (são "hashable").
#
# Dica: Você pode iterar sobre os itens (chave, valor) do dicionário original e adicionar `valor: chave` ao novo dicionário.
#
# Exemplo de uso:
# d_original = {'a': 1, 'b': 2, 'c': 3}
# print(inverter_dicionario(d_original))
#
# A saída esperada seria: {1: 'a', 2: 'b', 3: 'c'}

def inverter_dicionario(dicionario):
    novo_dicionario = {}
    
    for chave, valor in dicionario.items():
        novo_dicionario[valor] = chave
        
    return novo_dicionario
        
    
    
    
d_original = {'a': 1, 'b': 2, 'c': 3}
print(inverter_dicionario(d_original))
        
# achei relativamente tranquila, medo de quando o negocio começar a dificultar
    