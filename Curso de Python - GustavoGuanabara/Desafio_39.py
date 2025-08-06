# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade: Se ainda vai se alistar ao serviço miltar,
# se é a hora de se alistar ou, se já passou da hora de seu alistamento.
import datetime
nasc = int(input('Digite o ano em que você nasceu: '))
ano = int(str(datetime.date.today())[:4])
idade = ano - nasc
print('-'*40)
if idade < 17:
    print('Você tem {} anos. Faltam {} anos para o alistamento.'.format(idade,17 - idade))
elif idade == 17:
    print('Você tem {} anos, deverá se alistar este ano nas FFAA.'.format(idade))
elif idade == 18:
    print('Você tem {} anos e deverá se apresentar este ano para as FFAA.'.format(idade))
elif idade == 19:
    print('Você tem {} anos e deve estar servindo nas FFAA.'.format(idade))
elif idade == 20:
    print('Você tem {} anos e deve estar dando baixa, ou perdeu sua oportunidade de servir as FFAA.'.format(idade))
else:
    print('Ou você é reservista, ou já passou da hora de engressar nas FFAA.')

