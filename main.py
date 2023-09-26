# Dicionário para armazenar informações das contas
contas = {}

# Função para criar uma conta
def criar_conta():
    nome = input("Digite seu nome: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    numero_conta = input("Digite o número da conta: ")

    if numero_conta in contas:
        print("Número de conta já existe. Tente novamente.")
        return

    contas[numero_conta] = {
        "nome": nome,
        "saldo": saldo_inicial
    }

    print("Conta criada com sucesso!")

# Função para exibir informações da conta
def exibir_conta(numero_conta):
    if numero_conta in contas:
        conta = contas[numero_conta]
        print(f"Nome: {conta['nome']}")
        print(f"Saldo: {conta['saldo']}")
    else:
        print("Conta não encontrada.")

# Função principal
def main():
    while True:
        print("\nBem-vindo ao banco online!")
        print("1. Criar uma conta")
        print("2. Exibir informações da conta")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criar_conta()
        elif escolha == "2":
            numero_conta = input("Digite o número da conta: ")
            exibir_conta(numero_conta)
        elif escolha == "3":
            print("Obrigado por usar nosso banco online. Adeus!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()