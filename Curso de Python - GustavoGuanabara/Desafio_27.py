# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Primeiro nome: {}'.format(nome[0].capitalize()))
print('Último nome: {}'.format(nome[len(nome)-1].capitalize()))
