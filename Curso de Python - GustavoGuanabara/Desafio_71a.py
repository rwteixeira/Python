# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# ESTE CÓDIGO FOI DESENVOLVIDO POR RWT EM 19/10/2023
print('-'*30)
print('{:^30}'.format('BANCO R4'))
print('-'*30)
saque = int(input('Valor do saque: R$ '))
print('-'*30)
valor = saque
ced_50 = valor // 50
t20 = valor - (ced_50 * 50)
ced_20 = t20 // 20
t10 = t20 - (ced_20 * 20)
ced_10 = t10 // 10
t1 = t10 - (ced_10 * 10)
ced_1 = t1 // 1
if ced_50 != 0:
    print(f'{ced_50} cédulas de R$ 50,00')
if ced_20 != 0:
    print(f'{ced_20} cédulas de R$ 20,00')
if ced_10 != 0:
    print(f'{ced_10} cédulas de R$ 10,00')
if ced_1 != 0:
    print(f'{ced_1} cédulas de R$ 1,00')
print('-'*30)
print('Volte sempre - BANCO R4')
