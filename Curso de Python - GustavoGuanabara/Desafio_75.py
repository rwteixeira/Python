# Desafio_75: desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o número 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.
cont = i =0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
num = (n1,n2,n3,n4)
print('-'*30)
print(f'Você digitou os seguintes valores: {num}')
if num.count(9) == 0:
    print('O número 9 não apareceu nenhuma vez!')
else:
    print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado.')
print('Números pares:')
for n in num:
    if n % 2 == 0:
        print(n,end=' ')
