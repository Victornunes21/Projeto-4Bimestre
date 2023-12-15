import tkinter as tk
from tkinter import messagebox

class EscolaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento Escolar")
        
        # Criar uma instância da Escola
        self.escola = Escola("Escola Exemplo")
        
        # Botões para adicionar aluno, professor e disciplina
        self.add_student_button = tk.Button(root, text="Adicionar Estudante", command=self.adicionar_estudante)
        self.add_student_button.pack(pady=10)

        self.add_teacher_button = tk.Button(root, text="Adicionar Professor", command=self.adicionar_professor)
        self.add_teacher_button.pack(pady=10)

        self.add_discipline_button = tk.Button(root, text="Adicionar Disciplina", command=self.adicionar_disciplina)
        self.add_discipline_button.pack(pady=10)

    def adicionar_estudante(self):
        self.create_window("Adicionar Estudante", ["Nome do Estudante:", "Idade do Estudante:", "Matrícula do Estudante:"], self.add_student_to_school)

    def adicionar_professor(self):
        self.create_window("Adicionar Professor", ["Nome do Professor:", "Idade do Professor:", "Disciplina do Professor:"], self.add_teacher_to_school)

    def adicionar_disciplina(self):
        self.create_window("Adicionar Disciplina", ["Nome da Disciplina:", "Código da Disciplina:"], self.add_discipline_to_school)

    def create_window(self, title, labels, command):
        new_window = tk.Toplevel(self.root)
        new_window.title(title)

        entries = []
        for label_text in labels:
            tk.Label(new_window, text=label_text).pack()
            entry = tk.Entry(new_window)
            entry.pack()
            entries.append(entry)

        confirm_button = tk.Button(new_window, text="Adicionar", command=lambda: command(entries, new_window))
        confirm_button.pack(pady=10)

    def add_student_to_school(self, entries, window):
        nome = entries[0].get()
        idade = int(entries[1].get())
        matricula = entries[2].get()

        novo_estudante = Aluno(nome, idade, matricula)
        self.escola.admitir_estudante(novo_estudante)

        window.destroy()
        messagebox.showinfo("Sucesso", f"Estudante {nome} adicionado com sucesso!")

    def add_teacher_to_school(self, entries, window):
        nome = entries[0].get()
        idade = int(entries[1].get())
        disciplina = entries[2].get()

        novo_professor = Professor(nome, idade, disciplina)
        self.escola.contratar_professor(novo_professor)

        window.destroy()
        messagebox.showinfo("Sucesso", f"Professor {nome} adicionado com sucesso!")

    def add_discipline_to_school(self, entries, window):
        nome = entries[0].get()
        codigo = entries[1].get()

        nova_disciplina = Disciplina(nome, codigo)
        self.escola.criar_disciplina(nova_disciplina)

        window.destroy()
        messagebox.showinfo("Sucesso", f"Disciplina {nome} adicionada com sucesso!")

class Escola:
    def __init__(self, nome):
        self.nome = nome


class Aluno:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.disciplinas = {}
        # ...

    def adicionar_disciplina(self, disciplina):
        self.disciplinas[disciplina.codigo] = disciplina

    # Outros métodos para calcular média, notas, etc.

class Disciplina:
    def __init__(self, nome, codigo, professor):
        self.nome = nome
        self.codigo = codigo
        self.alunos_matriculados = []
        self.professor = professor
        self.notas = {}  # Dicionário para armazenar as notas dos alunos {matricula: nota}
        # ...

    def adicionar_aluno(self, aluno):
        self.alunos_matriculados.append(aluno)

    def adicionar_nota(self, aluno_matricula, nota):
        if aluno_matricula in self.notas:
            print("Nota já inserida para este aluno.")
        else:
            self.notas[aluno_matricula] = nota
            print(f"Nota {nota} adicionada para o aluno de matrícula {aluno_matricula}")

    # Outros métodos para gerenciar alunos, notas, etc.

class Professor:
    def __init__(self, nome, disciplinas_lecionadas):
        self.nome = nome
        self.disciplinas_lecionadas = disciplinas_lecionadas
        # ...

    def adicionar_nota_aluno(self, disciplina, aluno_matricula, nota):
        if disciplina.codigo in self.disciplinas_lecionadas:
            disciplina.adicionar_nota(aluno_matricula, nota)
        else:
            print("Você não leciona esta disciplina.")

    # Outros métodos para gerenciar notas, turmas, etc.

# Exemplo de uso:
professor1 = Professor("Dr. Silva", ["MAT123", "FIS456"])
aluno1 = Aluno("João", 18, "2023001")
aluno2 = Aluno("Maria", 19, "2023002")
matematica = Disciplina("Matemática", "MAT123", professor1)

matematica.adicionar_aluno(aluno1)
matematica.adicionar_aluno(aluno2)

professor1.adicionar_nota_aluno(matematica, aluno1.matricula, 8.5)
professor1.adicionar_nota_aluno(matematica, aluno2.matricula, 9.0)



# Inicializar o aplicativo Tkinter
root = tk.Tk()
app = EscolaApp(root)
root.mainloop()