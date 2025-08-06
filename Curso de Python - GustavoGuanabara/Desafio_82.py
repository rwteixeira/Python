# Desafio_82: Crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.
# ------------------------------------------------------------------------
#                     RESOLVIDO POR RWT EM 30/10/2023
# ------------------------------------------------------------------------
valores = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor: '))
    valores.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-='*20)
print(f'Lista Geral: {valores}')
print(f'Valores pares: {pares}')
print(f'Valores ímpares: {impares}')
