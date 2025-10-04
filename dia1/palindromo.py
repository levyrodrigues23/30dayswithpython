def calcular_palindromo(texto):
   texto = texto.replace(" ", "").lower()
   if texto == texto[::-1]:
       return True
   else:
       return False

   






lista_palindromos = input("Digite uma string, número ou qualquer coisa e eu vou verificar se é palíndromo ou não: ")
print(calcular_palindromo(lista_palindromos))


# --- Nova Questão: Verificador de Palíndromo ---
#
# Um palíndromo é uma palavra, frase ou número que se lê da mesma forma de trás para frente.
# Por exemplo: "arara", "ovo", "radar".
#
# Escreva uma função chamada `verificar_palindromo` que recebe uma string como argumento.
# A função deve retornar `True` se a string for um palíndromo e `False` caso contrário.
#
# Desafio extra: Faça sua função ignorar espaços e diferenças entre maiúsculas e minúsculas.
# Por exemplo, "Anotaram a data da maratona" deve ser considerado um palíndromo.
#
# Dica: Você pode usar o fatiamento de string `[::-1]` para inverter uma string facilmente.
# Para o desafio extra, os métodos de string `.replace()` e `.lower()` podem ser muito úteis.