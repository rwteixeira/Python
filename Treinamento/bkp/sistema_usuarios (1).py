from usuario import Usuario

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
