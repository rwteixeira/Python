# Desafio_96: Faça um programa que tenha uma função chamada área(),
# que receba  as  dimensões  de  um  terreno  retangular (largura e
# comprimento) e mostre a área do terreno.
# Ref: https://www.youtube.com/watch?v=oV1s53YGtvE
def área(larg,comp):
   a = larg * comp
   print(f'A área de um terreno {larg}x{comp} é de {a}m².')


# PROGRAMA PRINCIPAL
print(' Controle de Terrenos')
print('-'* 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l,c)