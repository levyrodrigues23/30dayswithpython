## 3o dias de programação em python
""" 
name = "jose"
las_name = "silva"
full_name = name + "  " + las_name
pais = "brasil"
cidade = "itapaje"
idade = 18
ano_nascimento = 2025 - idade
is_married = False
is_true = True
is_light_on = True


print(type(name))
print(type(las_name))
print(type(full_name))
print(type(pais))
print(type(cidade))
print(type(idade))
print(type(is_light_on))
print(type(ano_nascimento))
print(type(is_married))
print(type(is_true))

 """
 
from math import pi
 
def calcular_area_circulo(raio: float):
     area_of_circle = int(pi) * raio ** 2
     circumference_of_circle = 2 * int(pi) * raio
     return print(f"a area do circulo equivale a {area_of_circle} e a circunferencia equivale a {circumference_of_circle}")
     
     
usuario_raio = float(input("digite o valor do raio do circulo: "))
calcular_area_circulo(usuario_raio)