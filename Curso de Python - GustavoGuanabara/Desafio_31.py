distancia = float(input('Qual a distância de seu destino?: '))
if distancia > 200:
    print('Sua passagem custará R${:.2f}'.format(distancia * 0.45))
else:
    print('Sua passagem custará R${:.2f}'.format(distancia * 0.50))
