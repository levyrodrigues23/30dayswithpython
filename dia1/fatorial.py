def calcular_fatorial(numero):
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial = fatorial * i
    return fatorial

usuario = int(input("Digite um número para calcular o fatorial: "))
print(calcular_fatorial(usuario))
      
