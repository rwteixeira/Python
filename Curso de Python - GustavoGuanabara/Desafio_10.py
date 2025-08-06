vl = float(input('Quando dinheiro você tem na carteira?: '))
Cotacao = float(5.21)
conv = vl / Cotacao
print('Voce tem R${:.2f} reais que convertidos para dolar,\ndará US${:.2f} dólares'.format(vl,conv))
