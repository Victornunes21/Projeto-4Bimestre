class Tabuleiro:
    def __init__(self):
        # Inicializa o tabuleiro 3x3 vazio
        self.tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

    def exibir_tabuleiro(self):
        # Exibe o tabuleiro
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-----')

    def jogada_valida(self, linha, coluna):
        # Verifica se a jogada é válida
        return 0 <= linha < 3 and 0 <= coluna < 3 and self.tabuleiro[linha][coluna] == ' '

    def verificar_vitoria(self, simbolo):
        # Verifica se há um vencedor
        for i in range(3):
            if all(self.tabuleiro[i][j] == simbolo for j in range(3)) or \
               all(self.tabuleiro[j][i] == simbolo for j in range(3)):
                return True
        if all(self.tabuleiro[i][i] == simbolo for i in range(3)) or \
           all(self.tabuleiro[i][2 - i] == simbolo for i in range(3)):
            return True
        return False

    def tabuleiro_cheio(self):
        # Verifica se o tabuleiro está totalmente preenchido
        return all(self.tabuleiro[i][j] != ' ' for i in range(3) for j in range(3))

    def realizar_jogada(self, linha, coluna, simbolo):
        # Realiza a jogada no tabuleiro
        self.tabuleiro[linha][coluna] = simbolo


class Jogador:
    def __init__(self, simbolo):
        self.simbolo = simbolo

    def fazer_jogada(self, tabuleiro):
        while True:
            try:
                linha = int(input(f'Jogador {self.simbolo}, escolha a linha (0-2): '))
                coluna = int(input(f'Jogador {self.simbolo}, escolha a coluna (0-2): '))
                if tabuleiro.jogada_valida(linha, coluna):
                    tabuleiro.realizar_jogada(linha, coluna, self.simbolo)
                    break
                else:
                    print('Posição inválida. Escolha novamente.')
            except ValueError:
                print('Entrada inválida. Insira um número válido.')

def main():
    tabuleiro = Tabuleiro()
    jogador_X = Jogador('X')
    jogador_O = Jogador('O')
    jogador_atual = jogador_X

    while True:
        tabuleiro.exibir_tabuleiro()

        jogador_atual.fazer_jogada(tabuleiro)

        if tabuleiro.verificar_vitoria(jogador_atual.simbolo):
            tabuleiro.exibir_tabuleiro()
            print(f'Jogador {jogador_atual.simbolo} venceu!')
            break
        elif tabuleiro.tabuleiro_cheio():
            tabuleiro.exibir_tabuleiro()
            print('Empate!')
            break

        jogador_atual = jogador_O if jogador_atual == jogador_X else jogador_X

if __name__ == "__main__":
    main()