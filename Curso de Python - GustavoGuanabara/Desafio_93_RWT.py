# Desafio_93:  Crie um  programa que gerencie  o aproveitamento de um jogador
# de futebol. O programa  vai ler o nome  do  jogador e  quantas partidas ele
# jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final,
# tudo isso será gravado em um dicionário,  incluindo o  total de gols feitos
# durante o campeonato.
# Ref: https://www.youtube.com/watch?v=5yKiud-YNaE
# RESOLVIDO POR RWT EM 10/11/2023
campeonato = dict()
gols = []
campeonato['nome'] = str(input('Nome do jogador: '))
campeonato['partidas'] = int(input(f'Quantas partidas {campeonato["nome"]} jogou? '))
print('-'* 40)
for c in range(0, campeonato['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    campeonato['gols'] = gols
    campeonato['total'] = sum(gols)
print('-'* 40)
print(campeonato)
print(gols)
print('-'* 40)
for k, v in campeonato.items():
    print(f'O {k} tem o valor {v}.')
print('-'* 40)
for c in range(0,len(gols)):
    print(f'  - Na partida {c + 1}, {campeonato["nome"]} fez {gols[c]} gols')
