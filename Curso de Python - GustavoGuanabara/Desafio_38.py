# Escreva um programa que leia dois número e compare-os, mostrando na tela uma mensagem:
# Quem é maior, quem é menor e se existe igualdade entre eles.
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O número {} é MAIOR que o número {}'.format(n1,n2))
elif n2 > n1:
    print('O número {} é MAIOR que o número {}'.format(n2,n1))
else:
    print('Os números {} e {} são IGUAIS'.format(n1,n2))