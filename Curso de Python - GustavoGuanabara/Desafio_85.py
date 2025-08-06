# Desafio_85: Crie um programa onde o usuário possa digitar sete valores
# numéricos. Cadastre-os em uma lista única que mantenha separados os
# valores pares e ímpares. No final, mostre os valores pares e ímpares em
# ordem crescente.
# Ref: https://www.youtube.com/watch?v=2-fy24bbMJ4

valores = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º valor da lista: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
print('-'*30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
