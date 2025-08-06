# Declare 4 variáveis: id, do tipo inteiro; nome, do tipo string; salário, do tipo float; e brasileiro, do tipo boleano.
# Peça ao usuário para informar os valores dessas variáveis, mantendo seus tipos de dados.

id = int(input("Digite seu ID: "))
nome = str(input("Digite seu nome: "))
salario = float(input("Digite seu salário: "))
brasileiro = bool(input("Você é brasileiro: (True/False):"))


print(f"ID: {id}")
print(f"Nome: {nome}")
print(f"Salário: R${salario:.2f}")
print(f"Brasileiro: {brasileiro}")
