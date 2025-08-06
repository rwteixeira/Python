# Somar os múltiplos ímpares de 3 entre 1 e 500.
n = 500
s = 0
for i in range(1,n):
    mult = i / 3
    verif_1 = mult.is_integer()
    if verif_1 == True:
        verif_2 = i % 2
        if verif_2 != 0:
            s += i
print('A somatória dos múltiplos ímpares de 3 até 500 é {}'.format(s))
