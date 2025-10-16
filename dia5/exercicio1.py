# --- Dia 5: Exercício 1 - Sistema de Cadastro de Contatos ---
#
# Objetivo: Criar um programa de console para gerenciar uma lista de contatos.
#
# O programa deve usar uma lista para armazenar os contatos. Cada contato será um dicionário.
# Exemplo de um contato: {'nome': 'João Silva', 'telefone': '11999998888', 'email': 'joao.silva@email.com'}
#
# Funcionalidades a implementar:
# 1.  **Menu Principal:**
#     - O programa deve exibir um menu com as seguintes opções:
#       1. Adicionar Contato
#       2. Listar Contatos
#       3. Buscar Contato
#       4. Sair
#     - O programa deve continuar rodando em um laço `while True` até que o usuário escolha a opção "Sair".
#
# 2.  **Adicionar Contato:**
#     - Crie uma função `adicionar_contato(contatos)`.
#     - Peça ao usuário para digitar o nome, telefone e email do novo contato.
#     - Crie um dicionário com essas informações e adicione-o à lista de `contatos`.
#
# 3.  **Listar Contatos:**
#     - Crie uma função `listar_contatos(contatos)`.
#     - Se a lista estiver vazia, mostre uma mensagem "Nenhum contato cadastrado.".
#     - Se não, percorra a lista e imprima os detalhes de cada contato de forma organizada.
#
# 4.  **Buscar Contato:**
#     - Crie uma função `buscar_contato(contatos)`.
#     - Peça ao usuário para digitar o nome do contato que deseja buscar.
#     - Procure na lista por qualquer contato cujo nome contenha o texto buscado (pode ser uma busca parcial, "case-insensitive").
#     - Se encontrar, mostre os detalhes dos contatos encontrados.
#     - Se não encontrar, mostre uma mensagem "Contato não encontrado.".
#
# Dica: Estruture seu código com uma lista principal `contatos = []` e um laço `while` que controla o menu e chama as funções apropriadas.

# --- Funções Auxiliares ---
# Definimos todas as funções aqui, fora do menu.
contatos = []



def adicionar_contato():
    nome = input("digite o nome do contato que deseja adicionar: ")
    telefone = input("digite o telefone do contato: ")
    email = input("digite o email do contato: ")
    dicionario_contatos = {"nome": nome, "telefone": telefone, "email": email}
    contatos.append(dicionario_contatos)
    return print(f"{nome} foi adicionado com sucesso!")
    
    
def listar_contatos():
    if not contatos:
        print("nenhum contato cadastrado")
    else:
        for contato in contatos:
            print(f"contato: {contato["nome"]}, telefone: {contato["telefone"]}, email: {contato["email"]}")
            
        
        
    
def buscar_contatos():
    nome_buscar = input("digite o nome do contato que voce quer pesquisar: ")
    encontrados = False
    
    for contato in contatos:
        if nome_buscar.lower() in contato["nome"].lower():
            print(f"nome: {contato["nome"]}, telefone: {contato["telefone"]}, email: {contato["email"]}")
            encontrados = True
            
    if not encontrados:
        print("contato não foi localizado!")
            
        
        

    





def menu():
    
    while True:
        print("--- console para gerenciar uma lista de contatos ---")
        print("1. adicionar contatos")
        print("2. listar contatos")
        print("3. buscar contatos")
        print("4. sair")
        
        opcao = int(input("digite uma das opções: "))
        
        if opcao == 1:
            adicionar_contato()
        elif opcao == 2:
            listar_contatos()
            
        elif opcao == 3:
            buscar_contatos()
        elif opcao == 4:
            print("obrigado por nem sequer ter tentado usar esse negocio, agradeço demais :)")
            break
        else:
            print("sinto muito, mas voce digitou alguma opção errada!")
            continue
        

menu()
        
        
        
   
            
            
            






