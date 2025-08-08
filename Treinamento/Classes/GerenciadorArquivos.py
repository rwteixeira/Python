import os

class GerenciadorArquivos:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def listar_arquivos(self):
        return os.listdir(self.diretorio)

    def criar_arquivo(self, nome, conteudo=""):
        caminho = os.path.join(self.diretorio, nome)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)

    def ler_arquivo(self, nome):
        caminho = os.path.join(self.diretorio, nome)
        with open(caminho, "r", encoding="utf-8") as f:
            return f.read()

    def excluir_arquivo(self, nome):
        caminho = os.path.join(self.diretorio, nome)
        if os.path.exists(caminho):
            os.remove(caminho)
            return True
        return False

# Exemplo de uso
if __name__ == "__main__":
    gerenciador = GerenciadorArquivos(os.getcwd())

    gerenciador.criar_arquivo("teste.txt", "Olá, Ricardo!")
    print(gerenciador.ler_arquivo("teste.txt"))
    print(gerenciador.listar_arquivos())
    gerenciador.excluir_arquivo("teste.txt")
