# Desafio_87: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
# RESOLVIDO POR RWT EM 31/10/23

total = soma3col = 0
maior2lin = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
        if matriz[l][c] % 2 == 0:
            total += matriz[l][c]
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-'*30)
soma3col = matriz[0][2] + matriz[1][2] + matriz[2][2]

if matriz[1][0] > matriz[1][1]:
    if matriz[1][0] > matriz[1][2]:
        maior2lin = matriz[1][0]
    else:
        maior2lin = matriz[1][2]
elif matriz[1][1] > matriz[1][2]:
    maior2lin = matriz[1][1]
else:
    maior2lin = matriz[1][2]

print(f'A soma total de todos os elementos pares da matriz é {total}')
print(f'A soma da 3ª coluna da matriz é {soma3col}')
print(f'O maior valor da 2ª linha é {maior2lin}')
print('-'*30)