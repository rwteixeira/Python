# Crie uma Tupla preenchida com os 20 primeiros colocados da Tabela do
# Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados.
# C) uma lista com os times em ordem alfabética.
# D) Em que posição na Tabela está o time da Cuiabá.
times = ('Botafogo', 'Bragantino','Flamengo','Grêmio','Palmeiras','Athletico-PR','Atlético-MG','Fortaleza','Fluminense','Cuiabá','São Paulo','Internacional','Corinthians','Bahia','Cruzeiro','Vasco','Santos','Goiás','Coritiba','América-MG')
print('-'*30)
print('OS 5 PRIMEIROS COLOCADOS:')
#print('-'*30)
for cont in range(0, 5):
    print(f'{cont+1} - {times[cont]}')
print('-'*30)
print('OS 4 ÚLTIMOS COLOCADOS:')
#print('-'*30)
for cont in range(len(times) - 4, len(times)):
    print(f'{cont + 1} - {times[cont]}')
print('-'*30)
print('OS TIMES EM ORDEM ALFABÉTICA:')
classif = sorted(times)
for cont in classif:
    print(cont)
print('-'*30)
pesq = 0
clube = 'São Paulo'
for pesq in range(0,19):
    if times[pesq - 1] == clube:
        print(f'O time {clube} está na {pesq}ª posição do Campeonato Brasileiro.')
# SOLUÇÃO DIFERENTE PARA RESOLVER A LOCALIZAÇÃO DO TIME NA TABELA:
print(f'o time {clube} está na {times.index(clube) + 1}ª posição da tabela.')
