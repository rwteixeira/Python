# Desafio_90: Faça um programa que leia nome e média de um aluno, guardando também
# situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# Ref: https://www.youtube.com/watch?v=HipQYUk4koA&t=461s
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média do aluno {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-='*15)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')

