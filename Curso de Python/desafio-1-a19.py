# Crie um programa para emular uma quitanda. Crie uma tupla para armazenar
# as palávras "maça", "banana" e "laranja". Imprima cada um dos nomes das frutas,
# utilizando a tupla e uma estrutura do tipo for. Mostre a quantidade de elementos
# da tupla.
# 

tupla = ("maça", "banana", "laranja", "manga", "mamão")

tam = len(tupla)

for i in range(tam):
    print(f"{tupla[i]}",end=" ")

print(f"\nTamanho da tupla: {tam}")
