altura = float(input('Largura da parede: '))
largura = float(input('Altura da parede: '))
print('='*60)
area = largura * altura
tinta = area * 1/2
print('Para pintar {} m², serão necessários {} litros de tinta'.format(area,tinta))
print('='*60)
