# Crie um programa que peça para o usuário preencher o conteúdo de uma matriz
# de dimenções 3x4. Após inseridos os dados, realize uma busca na matriz e informe
# quais são os valores das linhas e colunas (posição) do maior e do menor elemento
# de toda a matriz.

# Inicializa a matriz 3x4 vazia
matriz = []

# Preenchimento da matriz pelo usuário
print("Preencha a matriz 3x4:")
for i in range(3):
    linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Inicializa variáveis para maior e menor valor
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

# Busca pelos valores máximo e mínimo
for i in range(3):
    for j in range(4):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        elif matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

# Exibe os resultados
print(f"\nMaior valor da matriz: {maior} na posição [linha {pos_maior[0]}][coluna {pos_maior[1]}]")
print(f"Menor valor da matriz: {menor} na posição [linha {pos_menor[0]}][coluna {pos_menor[1]}]")
