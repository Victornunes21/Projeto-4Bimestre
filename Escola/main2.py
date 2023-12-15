import tkinter as tk
from tkinter import messagebox

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = {}

    def adicionar_nota(self, disciplina, nota):
        self.notas[disciplina] = nota

    def ver_notas(self):
        return self.notas

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = {}

    def adicionar_disciplina(self, disciplina):
        self.disciplinas[disciplina] = {}

    def adicionar_nota(self, aluno, disciplina, nota):
        if disciplina in self.disciplinas and aluno in self.disciplinas[disciplina]:
            aluno.adicionar_nota(disciplina, nota)
            self.disciplinas[disciplina][aluno] = nota
            return True
        else:
            return False

    def __str__(self):
        return f"Professor: {self.nome}, Disciplinas: {list(self.disciplinas.keys())}"

class Diretor:
    def __init__(self):
        self.alunos = []
        self.professores = []

    def cadastrar_aluno(self, nome, idade):
        aluno = Aluno(nome, idade)
        self.alunos.append(aluno)
        return aluno

    def contratar_professor(self, nome):
        professor = Professor(nome)
        self.professores.append(professor)
        return professor

class EscolaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Escolar")

        self.diretor = Diretor()
        self.aluno_logado = None
        self.professor_logado = None

        self.label = tk.Label(root, text="Escolha o tipo de usuário:")
        self.label.pack(pady=10)

        self.aluno_button = tk.Button(root, text="Aluno", command=self.login_aluno)
        self.aluno_button.pack(pady=5)

        self.professor_button = tk.Button(root, text="Professor", command=self.login_professor)
        self.professor_button.pack(pady=5)

        self.diretor_button = tk.Button(root, text="Diretor", command=self.login_diretor)
        self.diretor_button.pack(pady=5)

    def login_aluno(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Insira seu nome:")
        self.label.pack(pady=10)

        self.entry_aluno = tk.Entry(self.root)
        self.entry_aluno.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.acessar_notas_aluno)
        self.login_button.pack(pady=5)

    def acessar_notas_aluno(self):
        nome_aluno = self.entry_aluno.get()
        for aluno in self.diretor.alunos:
            if aluno.nome == nome_aluno:
                self.aluno_logado = aluno
                self.exibir_notas_aluno()
                return

        messagebox.showerror("Erro", "Aluno não encontrado.")

    def exibir_notas_aluno(self):
        self.clear_screen()
        notas = self.aluno_logado.ver_notas()
        text = "Suas Notas:\n\n"
        for disciplina, nota in notas.items():
            text += f"{disciplina}: {nota}\n"
        self.label = tk.Label(self.root, text=text)
        self.label.pack()

    def login_professor(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Insira seu nome:")
        self.label.pack(pady=10)

        self.entry_professor = tk.Entry(self.root)
        self.entry_professor.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.acessar_professor)
        self.login_button.pack(pady=5)

    def acessar_professor(self):
        nome_professor = self.entry_professor.get()
        for professor in self.diretor.professores:
            if professor.nome == nome_professor:
                self.professor_logado = professor
                self.exibir_adicionar_notas()
                return

        messagebox.showerror("Erro", "Professor não encontrado.")

    def exibir_adicionar_notas(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Adicionar Notas")
        self.label.pack(pady=10)

        self.label_aluno = tk.Label(self.root, text="Nome do Aluno:")
        self.label_aluno.pack()
        self.entry_aluno = tk.Entry(self.root)
        self.entry_aluno.pack()

        self.label_disciplina = tk.Label(self.root, text="Disciplina:")
        self.label_disciplina.pack()
        self.entry_disciplina = tk.Entry(self.root)
        self.entry_disciplina.pack()

        self.label_nota = tk.Label(self.root, text="Nota:")
        self.label_nota.pack()
        self.entry_nota = tk.Entry(self.root)
        self.entry_nota.pack()

        self.adicionar_button = tk.Button(self.root, text="Adicionar", command=self.adicionar_nota)
        self.adicionar_button.pack(pady=5)

    def adicionar_nota(self):
        nome_aluno = self.entry_aluno.get()
        nome_disciplina = self.entry_disciplina.get()
        nota = self.entry_nota.get()

        for aluno in self.diretor.alunos:
            if aluno.nome == nome_aluno:
                aluno_encontrado = aluno
                break
        else:
            messagebox.showerror("Erro", "Aluno não encontrado.")
            return

        disciplinas_prof = self.professor_logado.disciplinas
        if nome_disciplina in disciplinas_prof:
            sucesso = self.professor_logado.adicionar_nota(aluno_encontrado, nome_disciplina, nota)
            if sucesso:
                messagebox.showinfo("Sucesso", "Nota adicionada com sucesso!")
                return

        messagebox.showerror("Erro", "Disciplina não encontrada ou aluno não matriculado.")

    def login_diretor(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Acesso Restrito - Diretor")
        self.label.pack(pady=10)

        self.cadastrar_aluno_button = tk.Button(self.root, text="Cadastrar Aluno", command=self.cadastrar_novo_aluno)
        self.cadastrar_aluno_button.pack(pady=5)

        self.cadastrar_professor_button = tk.Button(self.root, text="Cadastrar Professor", command=self.cadastrar_novo_professor)
        self.cadastrar_professor_button.pack(pady=5)

    def cadastrar_novo_aluno(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Cadastro de Novo Aluno")
        self.label.pack(pady=10)

        self.label_nome_aluno = tk.Label(self.root, text="Nome do Aluno:")
        self.label_nome_aluno.pack()
        self.entry_nome_aluno = tk.Entry(self.root)
        self.entry_nome_aluno.pack()

        self.label_idade_aluno = tk.Label(self.root, text="Idade do Aluno:")
        self.label_idade_aluno.pack()
        self.entry_idade_aluno = tk.Entry(self.root)
        self.entry_idade_aluno.pack()

        self.confirmar_cadastro_aluno = tk.Button(self.root, text="Cadastrar", command=self.confirmar_cadastro_aluno)
        self.confirmar_cadastro_aluno.pack(pady=5)

    def confirmar_cadastro_aluno(self):
        nome_aluno = self.entry_nome_aluno.get()
        idade_aluno = self.entry_idade_aluno.get()

        aluno_novo = self.diretor.cadastrar_aluno(nome_aluno, idade_aluno)
        messagebox.showinfo("Sucesso", f"Aluno {nome_aluno} cadastrado com sucesso!")

    def cadastrar_novo_professor(self):
        self.clear_screen()
        self.label = tk.Label(self.root, text="Cadastro de Novo Professor")
        self.label.pack(pady=10)

        self.label_nome_professor = tk.Label(self.root, text="Nome do Professor:")
        self.label_nome_professor.pack()
        self.entry_nome_professor = tk.Entry(self.root)
        self.entry_nome_professor.pack()

        self.confirmar_cadastro_professor = tk.Button(self.root, text="Cadastrar", command=self.confirmar_cadastro_professor)
        self.confirmar_cadastro_professor.pack(pady=5)

    def confirmar_cadastro_professor(self):
        nome_professor = self.entry_nome_professor.get()

        professor_novo = self.diretor.contratar_professor(nome_professor)
        messagebox.showinfo("Sucesso", f"Professor {nome_professor} cadastrado com sucesso!")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Inicializar o aplicativo Tkinter
root = tk.Tk()
app = EscolaApp(root)
root.mainloop()