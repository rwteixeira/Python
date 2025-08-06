# EXERCÍCIO 035
# Desenvolva um programa que leia o comprimento de 3 retas
# e diga ao usuário se elas podem ou não formar um triângulo.
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}
a = int(input('Digite o comprimento do lado A: '))
b = int(input('Digite o comprimento do lado B: '))
c = int(input('Digite o comprimento do lado C: '))
if a < (b+c):
    if a > (b-c):
        print('-'*30)
        print('Status: {}É possível!{}'.format(cores['azul'],cores['limpa']))
else:
    print('-' * 30)
    print('Status: {}Não é possível!{}'.format(cores['vermelho'],cores['limpa']))
