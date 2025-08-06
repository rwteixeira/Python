# Atividade: exemplo de como trabalhar com textos no Python.
# 26/11/2023 | Arquivos: email.txt, telefone.txt, mensagem.txt
# Ref: https://www.youtube.com/watch?v=AvUG8wZMh_E&list=PLs6lVkvJjKT5tFyuQuK-Zz96PeMhVk1BT&index=13

with open("email.txt", "r") as user_email:
    email = user_email.read()
    print(email)

with open("telefone.txt", "r") as user_cel:
    celular = user_cel.read()
    print(celular)

print('-'* 50)

with open("mensagem.txt", "r",encoding="utf-8") as mgs:
    mensagem = mgs.readlines()
for linha in mensagem:
    if "registro" in linha:
        print(linha)

print('-'* 50)
print('=== Arquivo só de leitura ===')
with open("senha.txt", "r") as arquivo:
    senha = arquivo.read()
    print(f'A senha é: {senha}')

# SUBSTITUI POR COMPLETO O TEXTO QUE ESTÁ ESCRITO
print('=== Arquivo de leitura e gravação ===')
with open("senha.txt", "w") as arquivo:
    arquivo.write("321_senha_123#$")

print('-'* 50)
# ADICIONA UMA INFORMAÇÃO AO TEXTO ORIGINAL
with open("email.txt","a") as arquivo:
    arquivo.write("\nrwteixeira2010@gmail.com")
