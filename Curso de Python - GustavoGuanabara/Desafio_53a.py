# PALÍNDROMO v.20
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um palíndromo!')
