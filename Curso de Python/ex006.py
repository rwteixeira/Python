# Crie um programa para praticar o uso de variáveis com entrada e saída de dados.
# Declare três variáveis, idade = 0, altura = 0.0 e nome = "".
# Peça para que o usuário informe a idade, altura e nome de uma pessoa, mantendo seus tipo s de dados,
# conforme o estabelecido durante a declaração das variáveis.
# Ao final, imprima na tela os dados informados pelo usuário, utilizando formatação por meio de f-strings.

idade = 0
altura = 0.0
nome = ""
idade = int(input("Informe a idade: "))
altura = float(input("Informe a altura: "))
nome = str(input("Informe o nome: "))
print(f"Idade: {idade} anos\n"
      f"Altura: {altura:.2f} metros\n"
      f"Nome: {nome}")
