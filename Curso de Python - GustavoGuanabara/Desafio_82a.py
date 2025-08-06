# Desafio_82: Crie um programa que vai ler vários números e colocar em uma
# lista. Depois disso, crie duas listas extras que vão conter apenas os
# valores pares e os valores ímpares digitados, respectivamente. Ao final,
# mostre o conteúdo das três listas geradas.
# Ref: https://www.youtube.com/watch?v=uk0gDFQEo_I

num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
num.sort()
print(f'A lista completa é {num}')
pares.sort()
print(f'A lista de pares é {pares}')
impares.sort()
print(f'A lista de ímpares é {impares}')
