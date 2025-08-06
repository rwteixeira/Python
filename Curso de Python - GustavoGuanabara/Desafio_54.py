# Crie um programa que leia a data de nascimento de sete pessoas.
# No final, mostre quantas ainda não completaram a maioridade e quantas já são maiores.
import datetime
Este_ano = int(str(datetime.date.today())[:4])
ac_1=0
ac_2=0
for c in range(1,8):
    num = int(input('Digite  {}º ano de nascimento: '.format(c)))
    idade = Este_ano - num
    if idade >= 21:
        print('Nasc: {} Idade: {} anos. Maior: SIM.'.format(num,idade))
        ac_1 += 1
    else:
        print('Nasc: {} Idade: {} anos. Maior: NÃO.'.format(num,idade))
        ac_2 += 1
print('-='*20)
print('{} pessoas já competaram a maioridade!'.format(ac_1))
print('{} pessoas ainda não completaram a maioridade!'.format(ac_2))