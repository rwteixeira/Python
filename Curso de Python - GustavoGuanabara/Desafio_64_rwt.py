# Desafio_64: Crie um programa que leia vários números inteiros pelo
# teclado.O programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. No final, mostre quantos números
# foram digitados e qual a soma entre eles (desconsiderando o flag).
# Resolvido: RWT
total = 0
cont = 0
num = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        print('Você saiu do programa!')
        exit()
    else:
        total = total + num
        cont = cont + 1
        print('A soma dos números digitados é {} e o número de entradas é {}'.format(total,cont))
print('você saiu do programa!')
