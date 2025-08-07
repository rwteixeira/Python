import os

# Caminho absoluto do diretório onde o script está salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))

# Caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_script, "exemplo.txt")

with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write("Arquivo salvo no mesmo diretório do script.")

print()
print(diretorio_script)
print()
print(caminho_arquivo)
print()