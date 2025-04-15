import sqlite3

# Conecta (ou cria) o banco
conn = sqlite3.connect("show_do_milhao.db")
cursor = conn.cursor()

# Cria a tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('aluno', 'professor')) NOT NULL
)
""")

# Inserindo alguns usuários de teste
usuarios_teste = [
    ("joao@aluno.com", "1234", "aluno"),
    ("maria@aluno.com", "abcd", "aluno"),
    ("prof.lucas@prof.com", "senha123", "professor")
]

# Inserindo os usuários se ainda não existem
for email, senha, tipo in usuarios_teste:
    try:
        cursor.execute("INSERT INTO usuarios (email, senha, tipo) VALUES (?, ?, ?)", (email, senha, tipo))
    except sqlite3.IntegrityError:
        # ignora se já estiver cadastrado
        pass

conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")
