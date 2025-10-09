# --- Nova Questão: Mesclar e Somar Dicionários ---
#
# Escreva uma função chamada `mesclar_dicionarios` que recebe dois dicionários como argumentos.
# Ambos os dicionários terão chaves como strings e valores como números inteiros.
#
# A função deve retornar um novo dicionário que contenha todas as chaves de ambos os dicionários de entrada.
# Se uma chave existir em ambos os dicionários, o valor no novo dicionário deve ser a soma dos valores dos dicionários de entrada.
#
# Dica: Você pode começar copiando um dos dicionários. Depois, itere sobre o segundo dicionário. Para cada chave, verifique se ela já existe no seu novo dicionário. Se existir, some os valores. Se não, apenas adicione a chave e seu valor.
#
# Exemplo de uso:
# dict1 = {'a': 100, 'b': 200, 'c': 300}
# dict2 = {'b': 50, 'c': 100, 'd': 400}
# print(mesclar_dicionarios(dict1, dict2))
#
# A saída esperada seria: {'a': 100, 'b': 250, 'c': 400, 'd': 400}