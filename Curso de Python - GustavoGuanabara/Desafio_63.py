# Desafio_63: Escreva um programa que leia um número n inteiro qualquer
# e mostre na tela os primeiros elementos de uma Sequência de Fibonacci.
print('=-'*15)
print('    SEQUÊNCIA DE FIBONACCI')
print('-='*15)
n = int(input('Quer exibir quantos termos? '))
t1 = 0 # Sempre será o mesmo valor.
t2 = 1 # Sempre será o mesmo valor.
print('-='*30)
print('{} → {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' → {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont = cont + 1
print(' FIM')
print('-='*30)
