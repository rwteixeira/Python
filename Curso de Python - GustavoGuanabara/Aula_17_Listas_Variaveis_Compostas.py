# FASE 17
# Variáveis Compostas: Listas
# Ao contrário das Tuplas, as Listas podem ser alteradas.
# As listas são limitadas por colchetes.
# Lista Original
# lanche = ['hamburger','suco','pizza','pudim']
lanche = ['hamburger','suco','pizza','pudim']
lanche[3] = 'sorvete'
lanche.append('cookie')
lanche.insert(0,'hotdog')
del lanche[3]
lanche.pop(3)
lanche.remove('suco')
lanche.pop()
if 'pizza' in lanche:
    lanche.remove('pizza')
print(lanche)
valores = list(range(4,11))
valor = [8,2,5,4,9,3,0]
print(valores)
print(valor)
valor.sort() # classifica a lista em ordem CRESCENTE
valor.sort(reverse=True) # classifica a lista em ordem DECRESCENTE
print(valor)
print(len(valor))
lanche.sort()
print(lanche)
valor.sort()
print(valor)
print('-'*40)
# **** AULA PRÁTICA ****
num = [2,5,9,1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
num.pop() # VAI REMOVER O ÚLTIMO VALOR DA LISTA
num.pop(2)
num.insert(2,3)
num.remove(3) # SE EXISTIREM 2 VALORES IGUAIS, O REMOVE REMOVERÁ A PRIMEIRA OCORRÊNCIA.
if 5 in num:
    num.remove(5)
    print('Número removido com sucesso!')
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')
print('-'*40)
# AULA PRÁTICA
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
valores.append(8)
valores.append(3)
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('-'*40) # **************************************
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')
print('-'*40) # **************************************
a = [2,3,4,7]
b = a[:]
b[2] = 8
print(f'lista A: {a}')
print(f'lista B: {b}')
