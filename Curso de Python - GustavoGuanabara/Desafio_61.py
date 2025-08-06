# Refaça o Desafio_051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressãousando a estrutura While.
# Ref: https://www.youtube.com/watch?v=vu5ehetQGe8&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=62
print('===========================================')
print('              TERMOS DE UMA PA             ')
print('===========================================')
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM')

