# Aula 4
# Crie um programa que imprima na tela, o nome, a idade, o salário e a nacionalidade de uma pessoa.
# Você vai imprimir tais dados utilizando formatação por meio de f-strings. Utilize caracteres de
# escape para melhor organizar sua formatação.

nome = "João"
idade = 30
salario = 2500.50
nacionalidade = "Brasileiro"   
print(f"Nome: {nome}\n"
      f"Idade: {idade} anos\n"
      f"Salário: R$ {salario:.2f}\n"
      f"Nacionalidade: {nacionalidade}")
