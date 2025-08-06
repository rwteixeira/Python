ano = int(input('Digite um ano qualquer: '))
verificador = (ano / 4).is_integer()
if verificador == True:
    print('Ano BISSEXTO!')
else:
    print('Ano não bissexto!')
