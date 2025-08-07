# ====================== LIDANDO COM ARQUIVOS =======================
# Crie um programa que peça e continue pedindo para que o usuário
# informe palavras e vá armazenando tais palavras em um arquivo. 
# Quando o usuário digitar '/exit', você deve interromper as leituras
# (a palavra '/exit' não deve ser armazenada no arquivo).
# Por fim, imprima na tela o conteúdo do arquivo.
# 

nome_arquivo = input("Nome do arquivo: ")

with open(nome_arquivo, 'w') as arquivo:
    while True:
        palavra = input("Digite um palavra: \033[33m/exit\033[m para encerrar: ").strip()
        if palavra == '/exit':
            break
        arquivo.write(f"{palavra}\n")

print("Palavras armazendas com sucesso!\n")

with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)