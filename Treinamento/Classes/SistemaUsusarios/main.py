import sqlite3

# Conectar ao banco de dados (cria o arquivo se não existir)
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Criar a tabela 'usuarios' se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    ativo BOOLEAN NOT NULL
)
""")
conn.commit()

# Funções do sistema
def adicionar_usuario(nome, email):
    try:
        cursor.execute("INSERT INTO usuarios (nome, email, ativo) VALUES (?, ?, ?)", (nome, email, False))
        conn.commit()
        print(f"Usuário '{nome}' cadastrado com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Erro: já existe um usuário com o email '{email}'.")

def ativar_usuario(email):
    cursor.execute("UPDATE usuarios SET ativo = ? WHERE email = ?", (True, email))
    if cursor.rowcount:
        conn.commit()
        print(f"Usuário com email '{email}' foi ativado.")
    else:
        print(f"Usuário com email '{email}' não encontrado.")

def desativar_usuario(email):
    cursor.execute("UPDATE usuarios SET ativo = ? WHERE email = ?", (False, email))
    if cursor.rowcount:
        conn.commit()
        print(f"Usuário com email '{email}' foi desativado.")
    else:
        print(f"Usuário com email '{email}' não encontrado.")

def listar_usuarios():
    cursor.execute("SELECT nome, email, ativo FROM usuarios")
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    for nome, email, ativo in usuarios:
        status = "Ativo" if ativo else "Inativo"
        print(f"Nome: {nome}\nEmail: {email}\nStatus: {status}")
        print("-" * 30)

def remover_usuario(email):
    cursor.execute("DELETE FROM usuarios WHERE email = ?", (email,))
    if cursor.rowcount:
        conn.commit()
        print(f"Usuário com email '{email}' removido com sucesso.")
    else:
        print(f"Usuário com email '{email}' não encontrado.")

# Menu interativo
def menu():
    while True:
        print("\n--- MENU DE USUÁRIOS ---")
        print("1. Cadastrar usuário")
        print("2. Ativar usuário")
        print("3. Desativar usuário")
        print("4. Listar usuários")
        print("5. Remover usuário")
        print("6. Sair")

        opcao = input("Escolha uma opção (1-6): ").strip()

        if opcao == '1':
            nome = input("Digite o nome do usuário: ").strip()
            email = input("Digite o email do usuário: ").strip()
            adicionar_usuario(nome, email)

        elif opcao == '2':
            email = input("Digite o email do usuário que deseja ativar: ").strip()
            ativar_usuario(email)

        elif opcao == '3':
            email = input("Digite o email do usuário que deseja desativar: ").strip()
            desativar_usuario(email)

        elif opcao == '4':
            print("\n--- LISTA DE USUÁRIOS ---")
            listar_usuarios()

        elif opcao == '5':
            email = input("Digite o email do usuário que deseja remover: ").strip()
            remover_usuario(email)

        elif opcao == '6':
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()

# Fechar conexão ao final
conn.close()

