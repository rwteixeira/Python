# Desafio_88: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites. O programa  vai perguntar quantos jogos serão  gerados e vai
# sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.
# Ref: https://www.youtube.com/watch?v=Hd7Ycaj61xE
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)
quant = int(input('Quantos jogos? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos): # i = índice, l = lista
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 4, '< BOA SORTE! >','-=' * 4)
