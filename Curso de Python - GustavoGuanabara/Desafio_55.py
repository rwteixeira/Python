# Leia o peso de 5 pessoas e avalie quem possui o maior e o menor peso.
maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('Entre com um valor para {}º o peso: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('-='*20)
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {} Kg'.format(menor))
