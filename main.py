MENU = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>"""

LIMITE_N_SAQUES = 3
saldo = 0
extrato = ""
n_saques = 0

def depositar(valor):
  global saldo
  global extrato
  if valor <= 0:
    print("\n***DEPÓSITO RECUSADO!***\nValor inválido!")
  else:
    saldo += valor
    print(f"Depósito de R${valor:.2f} efetuado com sucesso!")
    extrato += f"Deposito: R${valor:.2f}\n"

def sacar(valor):
  global saldo
  global extrato
  global n_saques
  if valor <= 0:
    print("\n***SAQUE RECUSADO!***\nValor inválido!")
  elif valor > 500:
    print(f"\n***SAQUE RECUSADO!***\nValor solicitado execede o valor limite!")
  elif n_saques >= LIMITE_N_SAQUES:
    print(f"\n***SAQUE RECUSADO!***\nQuantidade diaria de saques alcancada.")
  elif valor > saldo:
    print(f"\n***SAQUE RECUSADO!***\nValor solicitado execede o saldo atual!")
  else:
    saldo -= valor
    n_saques += 1
    print(f"Saque de R${valor:.2f} efetuado com sucesso!")
    extrato += f"Saque: R${valor:.2f}\n"

def exibir_extrato():
  print("\n\n====================EXTRATO====================")
  if extrato:
    print(extrato)
    print(f"\n\nSaldo: R${saldo:.2f}")
  else:
    print("Extrato vazio!")
  print("===============================================\n\n  ")

def main():

  while True:
    opcao = input(MENU)

    if opcao == 'q':
      break

    elif opcao == 'd':
      valor = round(float(input('Digite o valor a ser depositado: ')),3)
      depositar(valor)

    elif opcao == 's':
      valor = round(float(input('Digite o valor a ser sacado: ')),3)
      sacar(valor)

    elif opcao == 'e':
      exibir_extrato()

    else:
      print('Opção inválida!')


main()