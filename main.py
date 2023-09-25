def criar_conta():
    nome = input("Digite seu nome: ")
    numero_conta = input("Digite o número da conta: ")
    saldo = float(input("Digite o saldo inicial da conta: "))
    return {
        'nome': nome,
        'numero_conta': numero_conta,
        'saldo': saldo
    }

# Função para realizar um saque
def sacar(conta, valor):
    if conta['saldo'] >= valor:
        conta['saldo'] -= valor
        print(f"Saque de R${valor} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

# Função para realizar um depósito
def depositar(conta, valor):
    conta['saldo'] += valor
    print(f"Depósito de R${valor} realizado com sucesso.")

# Função para realizar uma transferência
def transferir(conta_origem, conta_destino, valor):
    if conta_origem['saldo'] >= valor:
        conta_origem['saldo'] -= valor
        conta_destino['saldo'] += valor
        print(f"Transferência de R${valor} realizada com sucesso para a conta {conta_destino['numero_conta']}.")
    else:
        print("Saldo insuficiente para a transferência.")

# Função principal
def main():
    conta1 = criar_conta()
    conta2 = criar_conta()

    while True:
        print("\nEscolha uma opção:")
        print("1. Sacar")
        print("2. Depositar")
        print("3. Transferir")
        print("4. Sair")
        
        escolha = input("Digite o número da opção: ")

        if escolha == '1':
            valor = float(input("Digite o valor para sacar: "))
            sacar(conta1, valor)
        elif escolha == '2':
            valor = float(input("Digite o valor para depositar: "))
            depositar(conta1, valor)
        elif escolha == '3':
            valor = float(input("Digite o valor para transferir: "))
            transferir(conta1, conta2, valor)
        elif escolha == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

    