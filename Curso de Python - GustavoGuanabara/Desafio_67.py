# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado
# for negativo.
# RESOLVIDO POR RWT EM 17/10/2023

num = tab = 0
while True:
    num = int(input('Informe a tabuada que deseja ver: '))
    if num < 0:
        break
    for i in range(1,11):
        print(f'{i} x {num} = {i * num}')
print('Você saiu do programa!')
