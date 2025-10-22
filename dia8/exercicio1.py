# --- Dia 8: Exercício 1 - Sistema de Biblioteca com POO ---
#
# Objetivo: Criar um sistema simples de biblioteca usando conceitos de Programação Orientada a Objetos.
#
# O sistema deve permitir:
# 1. Cadastrar livros e usuários
# 2. Emprestar e devolver livros
# 3. Consultar livros disponíveis e emprestados
#
# --- Classes a Implementar ---
#
# 1. Classe `Livro`:
#    - Atributos: titulo, autor, codigo, disponivel (booleano)
#    - Métodos: 
#      - `__init__()`: inicializador que recebe título, autor e código
#      - `emprestar()`: muda o status para indisponível
#      - `devolver()`: muda o status para disponível
#      - `__str__()`: retorna uma string formatada com as informações do livro
#
# 2. Classe `Usuario`:
#    - Atributos: nome, id, livros_emprestados (lista)
#    - Métodos:
#      - `__init__()`: inicializador que recebe nome e ID
#      - `emprestar_livro(livro)`: adiciona um livro à lista de emprestados
#      - `devolver_livro(livro)`: remove um livro da lista de emprestados
#      - `listar_livros()`: mostra todos os livros que o usuário possui emprestados
#
# 3. Classe `Biblioteca`:
#    - Atributos: livros (lista), usuarios (lista)
#    - Métodos:
#      - `__init__()`: inicializador que cria listas vazias
#      - `cadastrar_livro(livro)`: adiciona um livro ao acervo
#      - `cadastrar_usuario(usuario)`: adiciona um usuário ao sistema
#      - `emprestar_livro(codigo_livro, id_usuario)`: realiza o empréstimo
#      - `devolver_livro(codigo_livro, id_usuario)`: registra a devolução
#      - `listar_livros_disponiveis()`: mostra os livros que podem ser emprestados
#      - `listar_livros_emprestados()`: mostra os livros que estão emprestados e com quem
#
# --- Implementação ---
# Depois de criar as classes, crie um menu interativo que permita:
# 1. Cadastrar novo livro
# 2. Cadastrar novo usuário
# 3. Emprestar livro
# 4. Devolver livro
# 5. Listar livros disponíveis
# 6. Listar livros emprestados
# 7. Listar usuários e seus livros
# 8. Sair

# Seu código começa aqui...

# eu confesso que ainda não tenho muita habilidade com criação de classes extritamente no python, mas espero que essa atividade possa me situar um pouco sobre como esse paradigma de poo é aplicado nesta linguagem, que não seja tão diferente de java

class Livro:
    
    def __init__(self, titulo, autor, codigo, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel
        
    def emprestar(self, ):
        
        
    def devolver(self, )

class Usuario:
    
    
    def __init__(self, nome, id, livros_emprestados):
        
        
    
    
    
class Biblioteca:
    
    def __init__(self, livros, usuarios):
        pass





   
   
   
   
   
def menu():
    print("1. Cadastrar novo livro")   
    print("2. Cadastrar novo usuario")   
    print("3. emprestar livro")   
    print("4. devolver livro")   
    print("5. listar livros disponíveis")   
    print("6. listar livros emprestados")   
    print("7. listar usuarios e seus livros")   
    print("8. Sair")   
       
    opcao = int(input("escolha uma das opcoes: "))
    
    
    if opcao == 1:
        
    elif opcao == 2:
    elif opcao == 3:
    elif opcao == 4:
    elif opcao == 5:
    elif opcao == 6:
    elif opcao == 7:
    elif opcao == 8:
        print("obrigado por usar essa ferramenta ou nem sequer ter usado! tenha um ótimo dia!")
        break
    else:
        print("infelizmente voce acabou digitando uma opcao invalida! tente novamente!")
        continue
        
    
