v = int(input('Velocidade lida pelo radar: '))
m = 7
if v > 80:
    print('MULTADO! em R${:.1f} por excesso de velocidade!'.format((v - 80) * m))
else:
    print('SEM INFRAÇÃO!')
