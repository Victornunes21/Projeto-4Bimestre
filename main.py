# Lista para armazenar os nomes dos titulares das contas
titulares_contas = []
# Lista para armazenar os números das contas
numeros_contas = []
# Lista para armazenar os saldos das contas
saldos_contas = []

# Função para criar uma conta bancária
def criar_conta():
    nome = input("Digite o nome do titular da conta: ")
    numero_conta = input("Digite o número da conta: ")
    saldo_inicial = float(input("Digite o saldo inicial da conta: "))
    
    # Adicionar os dados às listas correspondentes
    titulares_contas.append(nome)
    numeros_contas.append(numero_conta)
    saldos_contas.append(saldo_inicial)
    
    print(f"Conta para {nome} criada com sucesso!")

# Função para depositar dinheiro em uma conta
def depositar():
    numero_conta = input("Digite o número da conta em que deseja depositar: ")
    valor_deposito = float(input("Digite o valor que deseja depositar: "))
    
    # Procurar a conta com o número especificado
    for i in range(len(numeros_contas)):
        if numeros_contas[i] == numero_conta:
            saldos_contas[i] += valor_deposito
            print(f"Depósito de R$ {valor_deposito:.2f} efetuado com sucesso na conta de {titulares_contas[i]}.")
            return
    
    print("Conta não encontrada. O depósito não pôde ser efetuado.")

def transferir():
    conta_origem = input("Digite o número da conta de origem: ")
    conta_destino = input("Digite o número da conta de destino: ")
    valor_transferencia = float(input("Digite o valor da transferência: "))
    
    # Procurar a conta de origem
    for i in range(len(numeros_contas)):
        if numeros_contas[i] == conta_origem:
            saldo_origem = saldos_contas[i]
            
            # Verificar se há saldo suficiente para a transferência
            if saldo_origem >= valor_transferencia:
                # Procurar a conta de destino
                for j in range(len(numeros_contas)):
                    if numeros_contas[j] == conta_destino:
                        saldos_contas[i] -= valor_transferencia
                        saldos_contas[j] += valor_transferencia
                        print(f"Transferência de R$ {valor_transferencia:.2f} efetuada com sucesso de {titulares_contas[i]} para {titulares_contas[j]}.")
                        return
    print("Conta de origem, conta de destino ou saldo insuficiente. A transferência não pôde ser efetuada.")
    
# Função para verificar saldo
def verificar_saldo():
    numero_conta = input("Digite o número da conta para verificar o saldo: ")
    
    # Procurar a conta com o número especificado
    for i in range(len(numeros_contas)):
        if numeros_contas[i] == numero_conta:
            print(f"Saldo da conta de {titulares_contas[i]}: R$ {saldos_contas[i]:.2f}")
            return
    
    print("Conta não encontrada. O saldo não pôde ser verificado.")

# Exemplo de uso das funções
while True:
    print("Opções:")
    print("1. Criar conta")
    print("2. Depositar dinheiro")
    print("3. Transferir dinheiro")
    print("4. Verificar saldo")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        criar_conta()
    elif opcao == '2':
        depositar()
    elif opcao == '3':
        transferir()
    elif opcao == '4':
        verificar_saldo()
    elif opcao == '5':
        break
    else:
        print("Opção inválida. Tente novamente.")

# Mostrar todas as contas criadas
print("Contas bancárias criadas:")
for i in range(len(titulares_contas)):
      print(f"Nome: {titulares_contas[i]}, Número da Conta: {numeros_contas[i]}, Saldo: R$ {saldos_contas[i]:.2f}")
