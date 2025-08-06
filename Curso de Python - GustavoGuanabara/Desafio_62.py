# Melhore o DESAFIO_61, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele
# disser que quer mostrar 0 termos.
print('===========================================')
print('              TERMOS DE UMA PA             ')
print('===========================================')
primeiro = int(input('Digite o primeiro termo da progressão: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))