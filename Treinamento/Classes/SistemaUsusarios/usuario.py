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
