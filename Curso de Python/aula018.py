# Crie um programa que peça para que o usuário informe o seu
# nome. Guarde o nome em uma variável. Em seguida, peça para
# que o usuário informe seu último nome e o armazene em outra
# variável, sobrenome.
# - Informe qual o comprimento de cada uma das variáveis;
# - Concatene as strings e mostre o resultado da concatenação,
# bem como o tamanho do resultado.
# 

nome = str(input("Nome: ")).upper().strip()
sobrenome = str(input("Sobrenome: ")).upper().strip()

print(f"\nNome completo: {nome} {sobrenome}")
print(f"Análise de tamanho: ")
print(f"Tamanho de Nome [{nome}] = {len(nome)}")
print(f"Tamanho de Sobrenome [{sobrenome}] = {len(sobrenome)}")
print(f"Tamanho total: Nome + Sobrenome = {len(nome) + len(sobrenome)}\n")