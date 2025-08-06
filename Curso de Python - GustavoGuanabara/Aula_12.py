# ANINHAMENTO CONDICIONAL
nome = str(input('Qual o seu nome? '))
if nome == 'Ricardo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Lisa Lucia Helenita Regina':
    print('Além de ser um belo nome, é bem familiar!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
