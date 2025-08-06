
cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m'}
print('-'*50)
s1 = float(input('Entre com a média do 1º Semestre: '))
s2 = float(input('Entre com a média do 2º Semestre: '))
media = (s1+s2)/2
print('-'*50)
if media < 5:
    print('Sua média final foi de {} - Status: {}REPROVADO!{}'.format(media,cores['vermelho'],cores['limpa']))
elif media >= 5 and media <=6.9:
    print('Sua média final foi de {} - Status: {}RECUPERAÇÃO!{}'.format(media,cores['amarelo'],cores['limpa']))
else:
    print('Sua média final foi de {} - Status: {}APROVADO!{}'.format(media,cores['azul'],cores['limpa']))
print('-'*50)