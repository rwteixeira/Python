# Desenvolva um programa que leia o primeiro termo
# de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.
#   ALTERADO DO ORIGINAL POR RWT EM 11/10/2023
print('===========================================')
print('              TERMOS DE UMA PA             ')
print('===========================================')
p = int(input('Digite o primeiro termo da progressão: '))
r = int(input('Digite a razão: '))
q = int(input('Defina a quantidade determos da PA: '))
decimo = p + (q - 1) * r + 1 # Fórmula matemática para calcular determinado termo.
for c in range(p,decimo,r):
    print('\033[33m{}\033[m'.format(c),end=' → ')
print('\033[36mACABOU\033[m')

