import tkinter as tk
from tkinter import messagebox

def abrir_tela_aluno():
    aluno_janela = tk.Toplevel()
    aluno_janela.title("Show do Milhão - Página do Aluno")
    aluno_janela.geometry("300x300")

    tk.Label(aluno_janela, text="Bem-vindo, Aluno!", font=("Arial", 14)).pack(pady=20)

    tk.Button(aluno_janela, text="Jogar", width=20, command=lambda: messagebox.showinfo("Jogar", "Iniciando o jogo...")).pack(pady=10)
    tk.Button(aluno_janela, text="Ranking", width=20, command=lambda: messagebox.showinfo("Ranking", "Exibindo o ranking...")).pack(pady=10)
    tk.Button(aluno_janela, text="Sair", width=20, command=aluno_janela.destroy).pack(pady=10)
