class Livro:
    def __init__(self, titulo, autor, editor):
        self.titulo = titulo
        self.autor = autor
        self.editor = editor

    def detalhes(self):
        return f"'{self.titulo}' - Editor: {self.editor}, escrito por {self.autor}"


livro = Livro("Python para Excel","Felix Zumstein", "O'REILLY")
print(livro.detalhes())
