# EXERCÍCIO 023 - REEDITADO COM CORES
# Faça um programa que leia um número entre 0 e 9999 e mostre na
# cada um dos dígitos separadamente.
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}
num = int(input('Entre com um número entre 0 e 9999: '))
print('-'*40)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Vamos analisar o número {}{}{}'.format(cores['azul'],num,cores['limpa']))
print('{}Unidade{}: {}{}{}'.format(cores['verde'],cores['limpa'],cores['amarelo'],u,cores['limpa']))
print('{}Dezena{}: {}{}{}'.format(cores['verde'],cores['limpa'],cores['amarelo'],d,cores['limpa']))
print('{}Centena{}: {}{}{}'.format(cores['verde'],cores['limpa'],cores['amarelo'],c,cores['limpa']))
print('{}Milhar{}: {}{}{}'.format(cores['verde'],cores['limpa'],cores['amarelo'],m,cores['limpa']))

print('-'*40)
