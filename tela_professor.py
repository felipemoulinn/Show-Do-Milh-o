import tkinter as tk
from tkinter import messagebox

def abrir_tela_professor():
    prof_janela = tk.Toplevel()
    prof_janela.title("Show do Milhão - Página do Professor")
    prof_janela.geometry("350x350")

    tk.Label(prof_janela, text="Bem-vindo, Professor!", font=("Arial", 14)).pack(pady=20)

    tk.Button(prof_janela, text="Cadastrar Pergunta", width=25, command=lambda: messagebox.showinfo("Cadastrar", "Cadastro de pergunta...")).pack(pady=10)
    tk.Button(prof_janela, text="Gerenciar Perguntas", width=25, command=lambda: messagebox.showinfo("Gerenciar", "Gerenciamento de perguntas...")).pack(pady=10)
    tk.Button(prof_janela, text="Ver Ranking", width=25, command=lambda: messagebox.showinfo("Ranking", "Visualizando ranking...")).pack(pady=10)
    tk.Button(prof_janela, text="Sair", width=25, command=prof_janela.destroy).pack(pady=10)
