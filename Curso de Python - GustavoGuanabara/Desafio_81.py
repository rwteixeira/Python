# Desafio_81: Crie um programa que vai ler vários números e colocar
# em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
cont = 0
lista = list()
while True:
    n = int(input('Digite um valor: '))
    cont += 1
    lista.append(n) # lista.append(int(input('Digite um valor: ')))
    opcao = str(input('Deseja continuar [S/N]: '))
    if opcao in 'Nn':
        break

lista.sort(reverse=True) # Ordem decrescente
print('-='*20)
print(f'Você digitou {cont} números') # Poderia ter usado: print(f' Você digitou {len(lista) valores.}')
print(lista)
if 5 in lista:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 NÃO faz parte da lista!')
