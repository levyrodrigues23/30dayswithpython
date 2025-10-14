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

def menu():
    dicionario_contatos = {}
    
    while True:
        opcao = input("digite a sua escolha: adicionar contato(a), listar contatos(b), buscar contatos(c), sair(d)")
        
        match opcao:
            case "a":
                def adicionar_contatos(contatos):
                    nome = input("digite o nome do novo contato: ")
                    telefone = input("digite o telefone do novo contato: ")
                    email = input("digite o email do novo contato: ")
                    
                    dicionario_contatos["nome"] = nome
                    dicionario_contatos["telefone"] = telefone
                    dicionario_contatos["email"] = email
                    
                    
                    
            case "b":
                def listar_contatos(contatos):
                    if contatos <= 0:
                        return print("nenhum contato cadastrado")
                    for nome, telefone, email in dicionario_contatos.items():
                        return nome, telefone, email
                        
                
            case "c":
                def buscar_contato(contatos):
                    contato_especifico = input("digite o contato que voce deseja buscar: ")
                    
            case "d":
                
           
            
                    
                        
        
