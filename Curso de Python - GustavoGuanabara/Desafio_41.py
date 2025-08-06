import datetime
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m'}
print('-'*50)
print('\033[1;37mSISTEMA DE QUALIFICAÇÃO DE ATLESTAS POR IDADE\033[m')
print('-'*50)
nasc = int(input('Digite o ano em que o atleta nasceu nasceu: '))
print('-'*50)
ano = int(str(datetime.date.today())[:4])
idade = ano - nasc
#print(idade)
if idade <= 9:
    print('Idade: {} anos - Qualificação: {}MIRIM{}'.format(idade,cores['amarelo'],cores['limpa']))
elif idade <= 14:
    print('Idade: {} anos - Qualificação: {}INFANTIL{}'.format(idade,cores['verde'],cores['limpa']))
elif idade <= 19:
    print('Idade: {} anos - Qualificação: {}JUNIOR{}'.format(idade,cores['azul'],cores['limpa']))
elif idade <=20:
    print('Idade: {} anos - Qualificação: {}SÊNIOR{}'.format(idade,cores['magenta'],cores['limpa']))
else:
    print('Idade: {} anos - Qualificação: {}MASTER{}'.format(idade,cores['vermelho'],cores['limpa']))
print('-'*50)