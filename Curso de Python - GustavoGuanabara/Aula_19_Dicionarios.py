# Dicionários:
# Variáveis Compostas
# Ref: https://www.youtube.com/watch?v=ZWj8o692qGY
#
dados = list()
dados.append('Pedro')
dados.append(25)
dados = dict()
dados = {'nome': 'Ricardo', 'idade': 59}
dados['sexo'] = 'M'
print(dados)
# REMOVER ELEMENTOS
del dados['idade']
print(dados)
# CRIANDO OUTRA LISTA
filme = {'titulo': 'Star Wars',
         'ano': 1977,
         'diretor': 'George Lucas'
        }
print(filme.values()) # Imprime os valores (Ex. Star Wars)
print(filme.keys()) # Imprime as chaves (Ex. titulo, diretor)
print(filme.items()) # Imprime tudo.
print('')
# ----------------------------
# LAÇO 'FOR'
for k, v in filme.items():
    print(f'O {k} é {v}')

print('')
# ----------------------------
# PRÁTICA
pessoas = {'nome': 'Ricardo', 'sexo': 'M', 'idade': 59}
print(pessoas['nome'])
print(pessoas['idade'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas)
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print('') # PARA PULAR UMA LINHA
# ACESSAR CHAVE, VALORES E ITENS POR LAÇO 'FOR'
for k in pessoas.keys():
    print(k)
print('') # PARA PULAR UMA LINHA
for k in pessoas.values():
    print(k)
print('') # PARA PULAR UMA LINHA
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('') # PARA PULAR UMA LINHA
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('') # PARA PULAR UMA LINHA
pessoas['nome'] = 'Wagner'
pessoas['sexo'] = 'M'
pessoas['peso'] = 85.8
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('') # PARA PULAR UMA LINHA

# CRIAR UM DICIONÁRIO DENTRO DE UMA LISTA
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    print('')
    brasil.append((estado.copy()))
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

