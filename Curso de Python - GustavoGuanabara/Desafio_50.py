# Das seis entradas, somar somente os números pares. Exercício NÃO resolvido por mim.
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('você informou {} números e a soma foi: {}'.format(cont,soma))
