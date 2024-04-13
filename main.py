# TODO:
# - [x] Função Saque deve rebecer os argumentos apenas por nome (keyword only) | (saldo = ..., valor = ...)

# - [x] Função Depositar deve receber argumentos apenas por posição (positional only) | (..., valor)

# - [x] Função Extrato deve receber argumentos por posição e por nome | (saldo, extrato = ...)

# - [ ] Criar função criar usuário 
  # - (Armazenar em uma lista de dicionários) | (nome, data_nascimento, cpf e endereço, [n_conta])
  # {cpf: {nome: ..., data_nascimento: ..., cpf: ..., endereco: ..., contas: [n_conta1, n_conta2, ...]}}
  # - Verificar se o usuário já existe antes de criar

# - [ ] Criar função criar conta corrente (associar usuário a conta)
  # - Armazenar contas em uma lista de dicionários onde a chave é o n_conta | (agencia, n_conta, cpf, saldo, extrato, n_saques)
  # {n_conta: {agencia: ..., cpf: ..., saldo: ..., extrato: ..., n_saques: ...}}

# - [ ] Criar função login
# - [ ] Criar função logout
# - [ ] Criar função listar contas
# - [ ] Criar função remover conta
# - [ ] Criar função remover usuário

MENU_PRINCIPAL = """
================ MENU ================
[c] Criar usuário
[a] Criar conta corrente
[lc] Listar contas
[l] Login
[q] Fechar o programa

==>"""



MENU_CONTA = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==>"""

LIMITE_N_SAQUES = 3
# lista de usuários [{cpf: {nome: ..., data_nascimento: ..., cpf: ..., endereco: ..., contas: [n_conta1, n_conta2, ...]}},
#                    {cpf: {nome: ..., data_nascimento: ..., cpf: ..., endereco: ..., contas: [n_conta1, n_conta2, ...]}}, ...]
_usuarios = []

# lista de contas [{n_conta: {agencia: ..., cpf: ..., saldo: ..., extrato: ..., n_saques: ...}},
#                  {n_conta: {agencia: ..., cpf: ..., saldo: ..., extrato: ..., n_saques: ...}}, ...]
_contas = []

def criar_usuario() -> dict:
  nome = input("Digite o nome do usuário: ")
  data_nascimento = input("Digite a data de nascimento do usuário: ")
  cpf = input("Digite o CPF do usuário: ")
  cpf_cadastrado = False
  if _usuarios:
    cpf_cadastrado = [True for usuario in _usuarios if cpf in usuario][0]
  if cpf_cadastrado:
    print("\n\n***ERRO: Usuário já cadastrado!***\n\n")
    return
  endereco = input("Digite o endereço do usuário: ")

  usuario = {
    cpf: {
      'nome': nome,
      'data_nascimento': data_nascimento,
      'cpf': cpf,
      'endereco': endereco,
      'contas': []
    }
  }

  return usuario 

def criar_conta_corrente() -> dict:
  agencia = input("Digite a agência da conta: ")
  cpf = input("Digite o CPF do usuário: ")
  cpf_cadastrado = any(cpf in usuario for usuario in _usuarios)
  if not cpf_cadastrado:
    print("\n\n***ERRO: Usuário não cadastrado!***\n\n")
    return
  saldo = 0.0
  extrato = ""
  n_saques = 0

  n_conta = str(len(_contas) + 1)
  # _usuarios[cpf]['contas'].append(n_conta)
  conta = {n_conta: {
    'agencia': agencia,
    'cpf': cpf,
    'saldo': saldo,
    'extrato': extrato,
    'n_saques': n_saques
  }}

  print(f"\n\n***Conta criada com sucesso!***\nNúmero da conta: {n_conta}\n\n")
  return conta

def logout():
  pass

def listar_contas():
  for conta in _contas:
    n_conta = list(conta.keys())[0]
    # print(f"Agência: {conta['agencia']}\nNúmero da conta: {conta['n_conta']}\nCPF: {conta['cpf']}\nSaldo: R${conta['saldo']:.2f}\n\n")
    print(f'Agência: {conta[n_conta]["agencia"]}\nNúmero da conta: {n_conta}\nCPF: {conta[n_conta]["cpf"]}\nSaldo: R${conta[n_conta]["saldo"]:.2f}\n\n')
def remover_conta():
  pass

def depositar(index, n_conta, valor):
  if valor <= 0:
    print("\n***DEPÓSITO RECUSADO!***\nValor inválido!")
  else:
    _contas[index][n_conta]['saldo'] += valor
    print(f"Depósito de R${valor:.2f} efetuado com sucesso!")
    _contas[index][n_conta]['extrato'] += f"Deposito: R${valor:.2f}\n"

def sacar(*, index, n_conta, valor):
  n_saques = _contas[index][n_conta]['n_saques']
  saldo = _contas[index][n_conta]['saldo']
  if valor <= 0:
    print("\n***SAQUE RECUSADO!***\nValor inválido!")
  elif valor > 500:
    print(f"\n***SAQUE RECUSADO!***\nValor solicitado execede o valor limite!")
  elif n_saques >= LIMITE_N_SAQUES:
    print(f"\n***SAQUE RECUSADO!***\nQuantidade diaria de saques alcancada.")
  elif valor > saldo:
    print(f"\n***SAQUE RECUSADO!***\nValor solicitado execede o saldo atual!")
  else:
    _contas[index][n_conta]['saldo'] -= valor
    _contas[index][n_conta]['n_saques'] += 1
    print(f"Saque de R${valor:.2f} efetuado com sucesso!")
    _contas[index][n_conta]['extrato'] += f"Saque: R${valor:.2f}\n"

def exibir_extrato(index,*,n_conta):
  saldo = _contas[index][n_conta]['saldo']
  extrato = _contas[index][n_conta]['extrato']
  print("\n\n====================EXTRATO====================")
  if extrato:
    print(extrato)
    print(f"\n\nSaldo: R${saldo:.2f}")
  else:
    print("Extrato vazio!")
  print("===============================================\n\n  ")

def menu_principal():
  while True:
    opcao = input(MENU_PRINCIPAL)

    if opcao == 'q':
      break

    elif opcao == 'c':
      usuario = criar_usuario()
      if usuario:
        _usuarios.append(usuario)

    elif opcao == 'a':
      conta = criar_conta_corrente()
      if conta:
        _contas.append(conta)
    
    elif opcao == 'lc':
      listar_contas()

    elif opcao == 'l':
      login()

    else:
      print('Opção inválida!')

def menu_conta(*, index, n_conta):
  while True:
    opcao = input(MENU_CONTA)

    if opcao == 'q':
      break

    elif opcao == 'd':
      valor = round(float(input('Digite o valor a ser depositado: ')),3)
      depositar(index, n_conta, valor)

    elif opcao == 's':
      valor = round(float(input('Digite o valor a ser sacado: ')),3)
      sacar(index=index, n_conta=n_conta, valor=valor)

    elif opcao == 'e':
      exibir_extrato(index, n_conta=n_conta)

    else:
      print('Opção inválida!')

def login():
  print("\n\n***LOGIN***\n")
  cpf = input("Digite o CPF: ")
  cpf_cadastrado = any(cpf in usuario for usuario in _usuarios)
  if not cpf_cadastrado:
    print("\n\n***ERRO: Usuário não cadastrado!***\n\n")
    return
  
  n_conta = input("Digite o número da conta: ")
  conta_cadastrada = any(n_conta in conta for conta in _contas) #TODO: Mesmo que a conta exista retorna False
  if not conta_cadastrada:
    print("\n\n***ERRO: Conta não cadastrada!***\n\n")
    return
  
  # Get index of the account
  index = [n_conta in conta for conta in _contas].index(True)
  print("\n\n***BEM VINDO!***\n\n")
  conta = _contas[index]
  menu_conta(index=index, n_conta=n_conta)


def main():
  menu_principal()

main()