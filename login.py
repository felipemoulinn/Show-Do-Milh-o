import sqlite3
import tkinter as tk
from tkinter import messagebox

# importa as funções das outras telas
from tela_aluno import abrir_tela_aluno
from tela_professor import abrir_tela_professor

def fazer_login():
    email = entrada_email.get()
    senha = entrada_senha.get()

    if "@aluno" in email:
        tipo_esperado = "aluno"
    elif "@prof" in email:
        tipo_esperado = "professor"
    else:
        messagebox.showerror("Erro", "O e-mail deve conter '@aluno' ou '@prof'.")
        return

    conn = sqlite3.connect("show_do_milhao.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE email = ? AND senha = ? AND tipo = ?
    """, (email, senha, tipo_esperado))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        messagebox.showinfo("Login", f"Bem-vindo, {tipo_esperado.capitalize()}!")
        if tipo_esperado == "aluno":
            abrir_tela_aluno()
        else:
            abrir_tela_professor()
    else:
        messagebox.showerror("Erro", "E-mail, senha ou tipo incorretos.")

# Interface gráfica da tela de login
root = tk.Tk()
root.title("Show do Milhão - Login")
root.geometry("300x250")

tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="E-mail:").pack()
entrada_email = tk.Entry(root, width=30)
entrada_email.pack(pady=5)

tk.Label(root, text="Senha:").pack()
entrada_senha = tk.Entry(root, show="*", width=30)
entrada_senha.pack(pady=5)

tk.Button(root, text="Entrar", command=fazer_login, width=20).pack(pady=15)

root.mainloop()
