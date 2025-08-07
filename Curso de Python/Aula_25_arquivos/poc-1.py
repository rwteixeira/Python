import os
diretorio = os.getcwd()

arquivo = str(input("Digite o nome do arquivo: "))

fqn = diretorio
# Cria (ou sobrescreve) um arquivo e escreve conteúdo nele
# with open("exemplo.txt", "w", encoding="utf-8") as arquivo:
#     arquivo.write("Olá, Ricardo!\n")
#     arquivo.write("Este é um exemplo de manipulação de arquivos.\n")

print(f"O nome e o caminho: {fqn}")
print() 
# print(f"O diretório de trabalho é: {diretorio}")

