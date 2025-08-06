# Inicializa a matriz 3x4 vazia
matriz = [[10, 20, 3, 4], [5, 60, 7, 8], [91, 10, 1, 2]]

# Preenchimento da matriz pelo usuário
# print("Preencha a matriz 3x4:")
# for i in range(3):
#     linha = []
#     for j in range(4):
#         valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
#         linha.append(valor)
#     matriz.append(linha)

maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        elif matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

print(f"\nMaior valor da Matriz: {maior} na posição [linha {pos_maior[0]}][coluna {pos_maior[1]}]")
print(f"Menor valor da Matriz: {menor} na posição [linha {pos_menor[0]}][coluna {pos_menor[1]}]\n")
