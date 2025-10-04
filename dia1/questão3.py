""" Exercício: Nível 3
Escreva um exemplo para diferentes tipos de dados Python, como Número (Inteiro, Flutuante, Complexo), String, Booleano, Lista, Tupla, Conjunto e Dicionário.
Encontre uma distância euclidiana entre (2, 3) e (10, 8)
🎉 PARABÉNS! 🎉 """

""" numero_inteiro = 10
numero_flutuante = 9.8
numero_complexo = 4 - 4j
string = "Olá, Mundo!"
booleano = True
lista = ['Asabeneh', 'Python', 'Finlândia']
tupla = ('Asabeneh', 'Python', 'Finlândia')
conjunto = {'Asabeneh', 'Python', 'Finlândia'}
dicionario = {'nome': 'jose', 'sobrenome': 'silva', 'pais': 'brasil'}
print(dicionario) """

from math import dist


def calcular_euclidiana(ponto1, ponto2):
    return dist(ponto1, ponto2)

ponto1 = (2, 3)
ponto2 = (10, 8)
print(calcular_euclidiana(ponto1, ponto2))