class PalavraSecreta:
    def __init__(self, palavra):
        self.palavra = palavra.upper()
        self.letras_descobertas = ['_' if letra.isalpha() else letra for letra in self.palavra]

    def revelar_letra(self, letra):
        letra = letra.upper()
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.letras_descobertas[i] = letra
            return True
        else:
            return False

    def palavra_descoberta(self):
        return '_' not in self.letras_descobertas

    def mostrar_palavra(self):
        return ' '.join(self.letras_descobertas)


class JogoDaForca:
    def __init__(self, palavra):
        self.palavra = PalavraSecreta(palavra)
        self.letras_erradas = []
        self.max_tentativas = 6

    def tentativa(self, letra):
        if letra.upper() in self.palavra.palavra:
            if not self.palavra.revelar_letra(letra):
                return False  # Letra correta, mas já tentada antes
        else:
            if letra.upper() not in self.letras_erradas:
                self.letras_erradas.append(letra.upper())
            else:
                return False  # Letra errada, mas já tentada antes

        return True

    def mostrar_status(self):
        print(f"Palavra: {self.palavra.mostrar_palavra()}")
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")
        print(f"Tentativas restantes: {self.max_tentativas - len(self.letras_erradas)}")

    def verificar_fim_jogo(self):
        if self.palavra.palavra_descoberta():
            print("Parabéns! Você descobriu a palavra!")
            return True
        elif len(self.letras_erradas) >= self.max_tentativas:
            print("Você excedeu o número máximo de tentativas. Fim de jogo!")
            print(f"A palavra era: {self.palavra.palavra}")
            return True
        else:
            return False


# Exemplo de utilização do jogo:

def main():
    palavra_secreta = "html"  # Palavra a ser adivinhada
    jogo = JogoDaForca(palavra_secreta)

    while not jogo.verificar_fim_jogo():
        jogo.mostrar_status()
        letra = input("Digite uma letra: ")
        if len(letra) == 1 and letra.isalpha():
            if not jogo.tentativa(letra):
                print("Letra já tentada antes. Tente outra.")
        else:
            print("Entrada inválida. Digite uma única letra.")

if __name__ == "__main__":
    main()

"""import tkinter as tk

class PalavraSecreta:
    def __init__(self, palavra):
        self.palavra = palavra.upper()
        self.letras_descobertas = ['_' if letra.isalpha() else letra for letra in self.palavra]

    def revelar_letra(self, letra):
        letra = letra.upper()
        if letra in self.palavra:
            for i, l in enumerate(self.palavra):
                if l == letra:
                    self.letras_descobertas[i] = letra
            return True
        else:
            return False

    def palavra_descoberta(self):
        return '_' not in self.letras_descobertas

    def mostrar_palavra(self):
        return ' '.join(self.letras_descobertas)

class JogoDaForca:
    def __init__(self, palavra):
        self.palavra = PalavraSecreta(palavra)
        self.letras_erradas = []
        self.max_tentativas = 6

    def tentativa(self, letra):
        if letra.upper() in self.palavra.palavra:
            if not self.palavra.revelar_letra(letra):
                return False  # Letra correta, mas já tentada antes
        else:
            if letra.upper() not in self.letras_erradas:
                self.letras_erradas.append(letra.upper())
            else:
                return False  # Letra errada, mas já tentada antes

        return True

    def mostrar_status(self):
        print(f"Palavra: {self.palavra.mostrar_palavra()}")
        print(f"Letras erradas: {', '.join(self.letras_erradas)}")
        print(f"Tentativas restantes: {self.max_tentativas - len(self.letras_erradas)}")

    def verificar_fim_jogo(self):
        if self.palavra.palavra_descoberta():
            print("Parabéns! Você descobriu a palavra!")
            return True
        elif len(self.letras_erradas) >= self.max_tentativas:
            print("Você excedeu o número máximo de tentativas. Fim de jogo!")
            print(f"A palavra era: {self.palavra.palavra}")
            return True
        else:
            return False

   

def iniciar_jogo():
    palavra_secreta = entry_palavra.get()
    jogo = JogoDaForca(palavra_secreta)

    def fazer_tentativa():
        letra = entry_letra.get()
        if len(letra) == 1 and letra.isalpha():
            if not jogo.tentativa(letra):
                status_label.config(text="Letra já tentada antes. Tente outra.")
            else:
                status_label.config(text="")
        else:
            status_label.config(text="Entrada inválida. Digite uma única letra.")

        jogo.mostrar_status()
        if jogo.verificar_fim_jogo():
            entry_letra.config(state='disabled')
            button_tentativa.config(state='disabled')

    window = tk.Tk()
    window.title("Jogo da Forca")

    label_palavra = tk.Label(window, text="Digite a palavra secreta:")
    label_palavra.pack()
    entry_palavra = tk.Entry(window)
    entry_palavra.pack()

    button_iniciar = tk.Button(window, text="Iniciar Jogo", command=fazer_tentativa)
    button_iniciar.pack()

    label_letra = tk.Label(window, text="Digite uma letra:")
    label_letra.pack()
    entry_letra = tk.Entry(window)
    entry_letra.pack()

    button_tentativa = tk.Button(window, text="Fazer Tentativa", command=fazer_tentativa)
    button_tentativa.pack()

    status_label = tk.Label(window, text="")
    status_label.pack()

    window.mainloop()

if __name__ == "__main__":
    iniciar_jogo()"""
