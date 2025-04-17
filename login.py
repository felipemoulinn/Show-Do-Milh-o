import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Importa as funções das outras telas
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

# Função para efeito hover no botão
def on_enter(e):
    entrar_btn['background'] = '#004080'  # Cor mais escura quando o mouse está sobre

def on_leave(e):
    entrar_btn['background'] = '#005A9E'  # Cor normal

# Interface gráfica da tela de login
root = tk.Tk()
root.title("Show do Milhão - Login")
root.geometry("300x300")  # Aumentei a altura para acomodar melhor o botão
root.configure(bg="#0078D7")

# Configuração do estilo para campos de entrada
style = ttk.Style()
style.configure("TEntry", padding=10, borderwidth=5, relief="flat", bordercolor="#ccc", focuscolor="#2ecc71")
style.map("TEntry", bordercolor=[("focus", "#2ecc71")])

# Frame principal
frame = tk.Frame(root, bg="#0078D7")
frame.pack(pady=30)

# Título
tk.Label(frame, text="Login", font=("Arial", 16, "bold"), bg="#0078D7", fg="white").pack(pady=10)

# Campo de e-mail
tk.Label(frame, text="Login (e-mail):", bg="#0078D7", fg="white").pack()
entrada_email = ttk.Entry(frame, width=20, style="TEntry")
entrada_email.pack(pady=5)

# Campo de senha
tk.Label(frame, text="Senha:", bg="#0078D7", fg="white").pack()
entrada_senha = ttk.Entry(frame, show="*", width=20, style="TEntry")
entrada_senha.pack(pady=5)

# Botão de entrar moderno
entrar_btn = tk.Button(
    frame,
    text="Entrar",
    command=fazer_login,
    width=15,
    height=2,
    bg="#005A9E",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    borderwidth=0,
    activebackground="#004080",
    activeforeground="white"
)
entrar_btn.pack(pady=20)

# Adicionando efeito hover
entrar_btn.bind("<Enter>", on_enter)
entrar_btn.bind("<Leave>", on_leave)

root.mainloop()