# Sistema bancario para cadastro de novos usuarios.
# Limite maximo de 10 transações diarias. 
# Mostrando no extrato data e hora das transações realizadas.

import datetime

clientes = {} 

def cadastro_novo_cliente():
    nome = input("Digite seu nome: ")
    cpf = input("Digite seu CPF: ")
    data_nascimento = input("Digite sua data de nascimento: ")
    endereco = input("Digite seu endereço: ")

    clientes[cpf] = {
        'nome': nome,
        'data_nascimento': data_nascimento,
        'endereco': endereco,
        'saldo': 0,
        'extrato': "",
        'saques_realizados': 0
    }
    print(f"Cliente {nome} cadastrado com sucesso!")


def deposito(cpf):
    if cpf not in clientes:
        print("Cliente não encontrado.")
        return

    valor = float(input("Informe o valor do depósito: "))

    if valor <= 0:
        print("Valor inválido!")
        return

    clientes[cpf]['saldo'] += valor
    data_hora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    clientes[cpf]['extrato'] += f"Depósito: R${valor:.2f} - {data_hora}\n"
    print("Depósito realizado com sucesso!")


def saque(cpf):
    if cpf not in clientes:
        print("Cliente não encontrado.")
        return

    valor = float(input("Informe o valor do saque: "))

    if valor <= clientes[cpf]['saldo'] and valor <= 500 and clientes[cpf]['saques_realizados'] < 3:
        data_hora = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        clientes[cpf]['extrato'] += f"Saque: R${valor:.2f} - {data_hora}\n"
        clientes[cpf]['saldo'] -= valor
        clientes[cpf]['saques_realizados'] += 1

        if clientes[cpf]['saques_realizados'] == 3:
            print("Limite de saques diários atingido!")
    else:
        print("Saldo insuficiente ou limite de saques excedido!")


def extrato(cpf):
    if cpf not in clientes:
        print("Cliente não encontrado.")
        return

    if clientes[cpf]['extrato'] == "":
        print("Não foram realizadas movimentações.")
    else:
        print("//////Extrato/////:")
        print(f"Nome do cliente: {clientes[cpf]['nome']}")
        print(clientes[cpf]['extrato'])
        print(f"Saldo: R${clientes[cpf]['saldo']:.2f}")


def sair():
    print("Obrigado por usar nossos serviços!\n")


menu = """
*****Menu*****

[c] Cadastrar novo cliente
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair

**************
"""

limite_transacoes_diarias = 10
transacoes_diarias = 0

while True:
    if transacoes_diarias >= limite_transacoes_diarias:
        print("Você atingiu o limite de transações diárias.")
        print("Pressione a tecla 'Q' para sair!")

    opcao = input(menu)

    if opcao == "c" or opcao == "C":
        cadastro_novo_cliente()

    elif opcao == "d" or opcao == "D":
        cpf = input("Digite o CPF do cliente: ")
        deposito(cpf)
        transacoes_diarias += 1

    elif opcao == "s" or opcao == "S":
        cpf = input("Digite o CPF do cliente: ")
        saque(cpf)
        transacoes_diarias += 1

    elif opcao == "e" or opcao == "E":
        cpf = input("Digite o CPF do cliente: ")
        extrato(cpf)
        transacoes_diarias += 1

    elif opcao == "q" or opcao == "Q":
        sair()
        break

    else:
        print("Opção inválida! Digite uma opção válida do menu.\n")
