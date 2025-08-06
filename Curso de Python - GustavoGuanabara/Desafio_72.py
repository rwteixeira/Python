# Crie um programa que tenha uma Tupla totalmente preenchida com uma
# contagem por extenso, de zero a vinte. Seu programa deverá ler o
# número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
# RESOLVIDO POR RWT EM 19/10/2023.
ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num < 0 or num > 20:
        num = int(input('Digite um número entre 0 e 20: '))
        break
    print(f'Você digitou o número \033[33m{ext[num]}\033[m')
