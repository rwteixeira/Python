import math

ct_1 = float(input('Valor do Cateto oposto: '))
ct_2 = float(input('Valor do Cateto Adjacente: '))
print('-'*35)
hip = math.sqrt((ct_1**2) + (ct_2**2))
print('Valor do Cat. Oposto: {}\nValor do Cat. Adjacente: {}\nComprimento da Hipotenusa: {:.2f}'.format(ct_1,ct_2,hip))
print('-'*35)