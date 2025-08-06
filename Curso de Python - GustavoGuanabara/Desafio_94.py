# Desafio_94: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando  os  dados  de  cada  pessoa  em  uma  lista. No  final,  mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.
# Ref: https://www.youtube.com/watch?v=ETnExBCFeps&t=13s
pessoa = dict() # INICIA A AQUISIÇÃO DE DADOS
cadastro = list()
soma_idade = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        resp = str(input('Continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-' * 30) # FIM DA AQUISIÇÃO DE DADOS
# INICIA A ANÁLISE DE DADOS
media = soma_idade / len(cadastro)
print(f'A) Nº de pessoas cadastradas: {len(cadastro)}.')
print(f'B) A média de idade do grupo: {media:5.2f}.')
print('C) As mulheres cadastradas são: ')
for p in cadastro:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ')
print()
print('D) Pessoas com idade acima da média de idade do grupo: ')
for i in cadastro:
    if i['idade'] >= media:
        for k, v in i.items():
            print(f'  - {k} = {v}')
        print()
