# Desafio_65: Crie um programa que leia vários números inteiros
# pelo teclado. No final da execução, mostre a média entre todos
# os valores e qual foi o maior e o menor valor lido. O programa
# deve perguntar ao usuário se ele quer ou não continuar a digitar
# valores.
op = 'S'
soma = cont = media = maior = menor = 0
while op in 'Ss':
    num = int(input('Digite um número inteiro: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
media = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont,media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
