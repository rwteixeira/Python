class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = False # Por padrão o usuário começa desativado.

    def ativar(self):
       self.ativo = True

    def desativar(self):
        self.ativo = False

    def exibir_dados(self):
        status = "Ativo" if self.ativo else "Inativo"
        print(f"Nome: {self.nome}\nEmail: {self.email}\nStatus: {status}")

usuario1 = Usuario("Ricardo Teixeira", "ricardo@email.com")
usuario1.exibir_dados()

usuario1.ativar()
usuario1.exibir_dados()
