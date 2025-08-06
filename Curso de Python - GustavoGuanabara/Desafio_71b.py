# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número
# inteiro) e o programa vai informar quantas cédulas de cada valor serão
# entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
# Ref: https://www.youtube.com/watch?v=_XGgwltYpYk
print('-'*30)
print('{:^30}'.format('BANCO R4'))
print('-'*30)
saque = int(input('Digite o valor do saque: R$ '))
print('-'*30)
total = saque
cedula = 50
qtde_cedulas = 0
while True:
    if total >= cedula:
        total = total - cedula
        qtde_cedulas = qtde_cedulas + 1
    else:
        if qtde_cedulas > 0:
            print(f'{qtde_cedulas} cédulas de R${cedula:.2f}')
        if cedula == 100:
            cedula = 50
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        qtde_cedulas = 0
        if total == 0:
            break
print('-'*30)
print('='*30)
print('Volte sempre ao Banco R4')