
import tkinter as tk
from tkinter import messagebox
import random

class JogoForca:
    def __init__(self, palavra):
        self.palavra = palavra.upper()
        self.palavra_escondida = ['_'] * len(palavra)
        self.tentativas = 6
        self.letras_usadas = set()

    def tentativa(self, letra):
        letra = letra.upper()
        if letra in self.letras_usadas:
            return  # Se a letra já foi usada, não faz nada
 
        self.letras_usadas.add(letra)

        if letra in self.palavra:
            for i, char in enumerate(self.palavra):
                if char == letra:
                    self.palavra_escondida[i] = letra
        else:
            self.tentativas -= 1

    def verificar_vitoria(self):
        return '_' not in self.palavra_escondida

    def verificar_derrota(self):
        return self.tentativas <= 0

    def obter_palavra_escondida(self):
        return ' '.join(self.palavra_escondida)


class JogoDaForcaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.palavras = ["PYTHON", "JAVASCRIPT", "JAVA", "HTML", "CSS", "RUBY", "PHP"]
        self.jogo = JogoForca(random.choice(self.palavras))

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(expand=True, padx=20, pady=20)

        self.label_palavra = tk.Label(self.frame_principal, text=self.jogo.obter_palavra_escondida(), font=('Arial', 18))
        self.label_palavra.pack()

        self.label_tentativas = tk.Label(self.frame_principal, text=f"Tentativas restantes: {self.jogo.tentativas}")
        self.label_tentativas.pack()

        self.letra_entry = tk.Entry(self.frame_principal, width=5)
        self.letra_entry.pack()

        self.botao_tentar = tk.Button(self.frame_principal, text="Tentar", command=self.tentar_letra)
        self.botao_tentar.pack()

        self.label_letras_usadas = tk.Label(self.frame_principal, text="Letras usadas:")
        self.label_letras_usadas.pack()

        self.label_lista_letras = tk.Label(self.frame_principal, text="", font=('Arial', 12))
        self.label_lista_letras.pack()

    def tentar_letra(self):
        letra = self.letra_entry.get()
        self.jogo.tentativa(letra)
        self.atualizar_interface()

    def atualizar_interface(self):
        self.label_palavra.config(text=self.jogo.obter_palavra_escondida())

        if self.jogo.verificar_vitoria():
            messagebox.showinfo("Parabéns!", "Boa guereiro(a)!")
            self.root.quit()

        if self.jogo.verificar_derrota():
            messagebox.showinfo("Game Over", f"A palavra era '{self.jogo.palavra}'. Você perdeu!")
            self.root.quit()

        self.label_tentativas.config(text=f"Tentativas restantes: {self.jogo.tentativas}")
        self.letra_entry.delete(0, tk.END)

        letras_usadas = ', '.join(sorted(self.jogo.letras_usadas))
        self.label_lista_letras.config(text=letras_usadas)


root = tk.Tk()
app = JogoDaForcaApp(root)
root.geometry("300x250")  # Definindo um tamanho para a janela
root.mainloop()