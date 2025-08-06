# Crie um programa que peça ao usuário para informar trÊs números com casas decimais.
# Calcule a média entre os três e mostre o resultado na tela, formatado para apresentar
# apenas duas casas decimais.

num1 = float(input("Entre com o preço da peça 1: "))
num2 = float(input("Entre com o preço da peça 2: "))
num3 = float(input("Entre com o preço da peça 3: "))

media = (num1 + num2 + num3)/3

print(f"A média dos valores é {media:.2f}")
