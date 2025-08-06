# Desafio_84: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
# Ref: https://www.youtube.com/watch?v=zPtvuLiEdKk

temp = list()
banco = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(banco) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    banco.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-*'*30)
# print(f'Os dados foram: {banco}')
print(f'Você cadastrou {len(banco)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in banco:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in banco:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
