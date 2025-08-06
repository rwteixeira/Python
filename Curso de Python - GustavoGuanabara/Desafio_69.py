# Desafio_69: Crie um programa que leia a idade de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
tot18 = totalH = mulher20 =0
homemvelho = mulhervelha = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totalH += 1
        if idade > homemvelho:
            homemvelho = idade
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'F':
        if idade > mulhervelha:
            mulhervelha = idade
    resp = ' '
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-'*30)
print('        ESTATÍSTICAS')
print('-'*30)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'O homem mais velho tem {homemvelho} anos')
print(f'A mulher mais velha tem {mulhervelha} anos')
print(f'Ao todo, temos {totalH} homens cadastrados')
print(f'Existem {mulher20} mulheres com menos de 20 anos')