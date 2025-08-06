# Desafio_74: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma Tupla. Depois disso, mostre a listagem de números
# gerados e também indique o menor e o maior valor que estão na Tupla.
# RESOLVIDO POR RWT EM 22/10/2023.

import random
maior = menor = 0
n1 = random.randint(0,99)
n2 = random.randint(0,99)
n3 = random.randint(0,99)
n4 = random.randint(0,99)
n5 = random.randint(0,99)
num = (n1,n2,n3,n4,n5)
for cont in range(0, len(num)):
    if cont == 0:
        maior = menor = num[cont]
    else:
        if num[cont] > maior:
            maior = num[cont]
        if num[cont] < menor:
            menor = num[cont]
print(num)
print(f'Maior: {maior}\nMenor: {menor}')
