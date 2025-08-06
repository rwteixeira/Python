# Listas - Parte II
# Ref: https://www.youtube.com/watch?v=YV_JQmZNFsk
# Variáveis compostas
Ref: https://www.youtube.com/watch?v=YV_JQmZNFsk
# -------------------------------------------------
print('-='*40)
dados = list()
dados.append('Pedro')
dados.append(25)

pessoas = [['Pedro',25],['Maria',19],['João',32]]
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0][0])
print(pessoas[0][1])
print(pessoas[1][0])
print(pessoas[1][1])
print(pessoas[1])
print('-='*40)
# -------------------------------------------------
teste = list()
teste.append('Ricardo')
teste.append(59)
galera = list()
galera.append(teste[:])
teste[0] = 'Lucia'
teste[1] = 60
galera.append(teste[:])
print(galera)
print('-='*40)
# -------------------------------------------------
galera = [['Lisa', 17], ['Ana', 22], ['Arthur', 34], ['Lucia', 60], ['Ricardo', 59]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')
# -------------------------------------------------
print('-='*40)
galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')
