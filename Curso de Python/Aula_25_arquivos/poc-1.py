import os

# Cria (ou sobrescreve) um arquivo e escreve conteúdo nele
with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá, Ricardo!\n")
    arquivo.write("Este é um exemplo de manipulação de arquivos.\n")

diretorio = os.getcwd()
os.