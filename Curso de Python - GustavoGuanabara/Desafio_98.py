# Desafio_98: Faça um programa que  tenha uma função  chamada contador(),
# que receba três parâmetros: início, fim e passo  e  realize a contagem.
# Seu programa tem que realizar três  contagens através da função criada:
# Ref: https://www.youtube.com/watch?v=DCBlt_z2UOE
# a) De 1 até 10, de 1 em 1.
# b) De 10 até 0, de 2 em 2.
# c) Uma contagem personalizada.
temp = 0
from time import sleep

# def contador(i,f,p):

# SITUAÇÃO <<< A >>>
for i in range(1, 11, 1):
    print(f' {i}',end='')
    sleep(0.25)
print('\033[36m FIM\033[m')

# SITUAÇÃO <<< B >>>
for i in range(10, 0, 2):
    print(f' {i}',end='')
    sleep(0.25)
print('\033[36m FIM\033[m')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


print('\033[33mFIM\033[m')