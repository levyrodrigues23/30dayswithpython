# --- Dia 5: Exercício 2 - Simulador de Caixa Eletrônico (ATM) ---
#
# Objetivo: Criar um programa que simula as operações básicas de um caixa eletrônico.
#
# O programa deve manter o controle do saldo do usuário e um histórico de transações.
#
# Funcionalidades a implementar:
# 1.  **Estado Inicial:**
#     - Comece com um saldo inicial, por exemplo, `saldo = 1000.00`.
#     - Crie uma lista vazia para o histórico, por exemplo, `historico = []`.
#
# 2.  **Menu Principal:**
#     - Exiba um menu com as opções:
#       1. Ver Saldo
#       2. Depositar
#       3. Sacar
#       4. Ver Histórico
#       5. Sair
#     - Use um laço `while True` para manter o programa ativo.
#
# 3.  **Ver Saldo:**
#     - Crie uma função `ver_saldo(saldo)`.
#     - A função deve simplesmente imprimir o saldo atual formatado como moeda (ex: "R$ 1000.00").
#
# 4.  **Depositar:**
#     - Crie uma função `depositar(saldo, historico)`.
#     - Peça ao usuário o valor que deseja depositar.
#     - Valide se o valor é positivo.
#     - Adicione o valor ao saldo e registre a operação no histórico (ex: "Depósito: +R$ 200.00").
#     - A função deve retornar o novo saldo.
#
# 5.  **Sacar:**
#     - Crie uma função `sacar(saldo, historico)`.
#     - Peça ao usuário o valor que deseja sacar.
#     - Verifique se o valor é positivo e se há saldo suficiente na conta.
#     - Se o saque for possível, subtraia o valor do saldo e registre no histórico (ex: "Saque: -R$ 150.00").
#     - Se não for possível, exiba uma mensagem de erro (ex: "Saldo insuficiente.").
#     - A função deve retornar o novo saldo.
#
# 6.  **Ver Histórico:**
#     - Crie uma função `ver_historico(historico)`.
#     - Imprima todas as transações registradas na lista de histórico.


saldo = 1000
