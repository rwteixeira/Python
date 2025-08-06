# Crie um programa que leia dois valores e mostre um menu com os
# seguintes comandos: 1) Somar 2) Multiplicar 3) Maior
# 4) Novos números 5) Sair do programa
# Seu programa deverá realizar a operação em cada caso.
from time import sleep
print('\033[32m-=\033[m'*15)
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
print('\033[32m-=\033[m'*15)
while opcao != 5:

    print('''Selecione a opção desejada:
 [1] SOMAR
 [2] MULTIPLICAR
 [3] MAIOR
 [4] NOVOS NÚMEROS
 [5] SAIR''')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado da multiplicação dos números {} e {} é {}'.format(
            n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            print('O número {} é maior que {}.'.format(n1, n2))
        else:
            print('O número {} é maior que {}.'.format(n2, n1))
    elif opcao == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('o programa está sendo finalizado.')
    else:
        print('Opção inválida!! Tente novamente!')
    sleep(3)
print('\033[33mFechando...\033[m')
