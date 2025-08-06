# Faça um programa que leia uma frase pelo teclado
# e mostre:
# 1) Quantas vezes aparece a letra 'A';
# 2) Em que posição ela aparece a primeira vez;
# 3) Em que posição ela aparece pela última vez.
frase = str(input('Escreva uma frase para análise: ')).upper().strip()
print('-'*50)
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A')+1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A')+1))
print('-'*50)
