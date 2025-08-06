# LISTAS
# Declare uma lista vazia. Em seguida, solicite ao usuário que informe os 5 elementos
# que serão armazenados na lista - utilize o append(). Calcule a média entre os elementos
# da lista e mostre o resultado na tela. Imprima o conteúdo de cada um dos elementos
# da lista, individualmente, na tela.
# 
mt = 5
lista = []
for i in range(1, 6):
    elemento = float(input(f"Entre com o valor do {i}º elemento: "))
    lista.append(elemento)
    media = sum(lista)/5
print()    
print("---"*10)

# MÉTODO 1
for e in lista:
    print(e," ",end="")
print()    
print("---"*10)

# MÉTODO 2
for i in range(0, 5):
    print(lista[i]," ",end="")
print()
print("---"*10)
print(f"A média dos 5 elementos é: {media}")
print()



