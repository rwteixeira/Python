# Crie uma lista denominada mat. Adicione outras três sub-listas a mat,
# cada uma delas com os respectivos elementos:
#
# I.    sub-lista 1: 1, 2, 3
# II.   sub-lista 2: 4, 5, 6
# III.  sub-lista 3: 7, 8, 9
# 
# Imprima todos os elementos da primeira linha, utilizando mat
# dentro de um laço. 
# 
# Imprima todos os elementos numéricos armazenados em mat,
# utilizando laços.
# 
mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ] 
print("Elementos da primeira linha")
for i in mat[0]:
    print(i, end=' ')

print()
print("Elementos da Matriz")
for linha in mat:
    for elem in linha:
        print(elem, end=' ')
    print()