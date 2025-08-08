class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = False

    def ativar(self):
        self.ativo = True

    def desativar(self):
        self.ativo = False

    def exibir_dados(self):
        status = "Ativo" if self.ativo else "Inativo"
        print(f"Nome: {self.nome}\nEmail: {self.email}\nStatus: {status}")


class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome, email):
        if self.buscar_usuario_por_email(email):
            print(f"Usuário com email '{email}' já existe.")
            return
        novo_usuario = Usuario(nome, email)
        self.usuarios.append(novo_usuario)
        print(f"Usuário '{nome}' adicionado com sucesso.")

    def buscar_usuario_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        return None

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        for usuario in self.usuarios:
            usuario.exibir_dados()
            print("-" * 30)

    def remover_usuario(self, email):
        usuario = self.buscar_usuario_por_email(email)
        if usuario:
            self.usuarios.remove(usuario)
            print(f"Usuário com email '{email}' removido com sucesso.")
        else:
            print(f"Usuário com email '{email}' não encontrado.")


# Menu interativo
def menu():
    sistema = SistemaUsuarios()

    while True:
        print("\n--- MENU DE USUÁRIOS ---")
        print("1. Cadastrar usuário")
        print("2. Ativar usuário")
        print("3. Listar usuários")
        print("4. Remover usuário")
        print("5. Sair")

        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == '1':
            nome = input("Digite o nome do usuário: ").strip()
            email = input("Digite o email do usuário: ").strip()
            sistema.adicionar_usuario(nome, email)

        elif opcao == '2':
            email = input("Digite o email do usuário que deseja ativar: ").strip()
            usuario = sistema.buscar_usuario_por_email(email)
            if usuario:
                usuario.ativar()
                print(f"Usuário '{usuario.nome}' foi ativado com sucesso.")
            else:
                print(f"Usuário com email '{email}' não encontrado.")

        elif opcao == '3':
            print("\n--- LISTA DE USUÁRIOS ---")
            sistema.listar_usuarios()

        elif opcao == '4':
            email = input("Digite o email do usuário que deseja remover: ").strip()
            sistema.remover_usuario(email)

        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


# Executar o menu
menu()
