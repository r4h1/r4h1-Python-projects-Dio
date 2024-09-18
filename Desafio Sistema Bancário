# Algoritimo para sistema bancário

saldo = 0
limite_por_saque = 500.0
extrato_str = ""
saques_realizados = 0
limite_maximo_saques_diarios = 3

def deposito():

  global saldo, extrato_str
  valor = float(input("Informe o valor do depósito: "))

  if valor <= 0:
    print("Valor invalido!")
    return

  saldo += valor
  extrato_str += f"Depósito: R${valor:.2f}\n"

  return valor

def saque():
  global saldo, extrato_str, saques_realizados, valor

  valor = float(input("Informe o valor do Saque: "))

  if valor <= saldo and valor <= limite_por_saque and saques_realizados < limite_maximo_saques_diarios:
    extrato_str += f"Saque: R${valor:.2f}\n"
    saldo -= valor
    saques_realizados += 1

    if saques_realizados == limite_maximo_saques_diarios:
      print("Limite de saques diários atingido!")

  else:
    print("Saldo insuficiente!")
  return valor

def extrato(): 

  if extrato_str == "":
    print("Não foram realizadas movimentações.")
  else:
    print("Aqui está seu extrato")
    print(extrato_str) 
    print(f"Seu saldo é de R${saldo:.2f}")

def sair():
  print("Obrigado por usar nossos serviços!\n")

menu = """
*****Menu*****

[s] Saque
[d] Deposito
[e] Extrato
[q] Sair

**************
"""

while True:
    opcao = input(menu)

    if opcao == "d" or opcao == "D":
        # valor = float(input("Informe o valor do depósito: "))
        deposito()

    elif opcao == "s" or opcao == "S":
        # valor = float(input("Informe o valor do saque: "))
        saque()

    elif opcao == "e" or opcao == "E":
      extrato()

    elif opcao == "q" or opcao == "Q":
      sair()
      break

    else:
      print("Opção invalida! Digite uma opção valida do menu.\n")
