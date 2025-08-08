class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")


ricardo = Pessoa("Ricardo", 60)
lucia = Pessoa("Lucia", 61)
roberto = Pessoa("Roberto", 55)


ricardo.apresentar()
lucia.apresentar()
roberto.apresentar()
