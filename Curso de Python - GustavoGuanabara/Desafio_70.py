# Crie um programa que leia o nome de vários produtos. O programa
# deverá perguntar se o usuário vai continuar. No final, mostre:
# A) Qual é o total gasto.
# B) Quantos produtos custam mais de R$ 1.000.
# C) Qual é o nome do produto mais barato.
total = prod_caro = prod1000 = prod_barato = cont = 0
ref_preco = 0
nome_prod_caro = ''
nome_prod_barato = ''
while True:
    produto = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        prod1000 += 1
    if cont == 1 or preco < prod_barato:
        prod_barato = preco
        nome_prod_barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^45}'.format(' FIM DO PROGRAMA '))
print('-'*45)
print('{: ^45}'.format('ESTATÍSTICAS'))
print('-'*45)
print(f'Total da compra: R${total:.2f}')
print(f'{prod1000} Produtos acima de R$ 1.000,00')
#print(f'Produto {nome_prod_caro} é o mais caro da compra e custa: R${prod_caro:.2f}')
print(f'{nome_prod_barato} é o produto mais barato e custa R${prod_barato:.2f}')
