# Desafio_78: Faça um programa que leia 5 valores numéricos
# e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e as suas respectivas posições na lista.
# Ref: https://www.youtube.com/watch?v=q8Z1cRdJnfk
#
maior = menor = 0
valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]

        if valores[c] < menor:
            menor = valores[c]
print('-'*50)
print(f'Você digitou os seguintes valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i+1} - ', end='') # O incremento de 1 para o índice 'i' é opcional.
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1} - ', end='') # O incremento de 1 para o índice 'i' é opcional.
print()
print('-'*50)
