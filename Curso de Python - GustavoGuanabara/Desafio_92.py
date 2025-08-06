# Desafio_92: Crie um programa que leia  nome, ano de nascimento e  carteira  de trabalho
# e cadastre-os (com idade) em um dicionário se, por acaso, a CTPS for diferente de zero,
# o dicinário receberá também, o  ano de  contratação e o  salário. Calcule e acrescente,
# além da idade, com quantos anos a pessoa vai se aposentar.
# Ref: https://www.youtube.com/watch?v=Vsqemzdrj78
import datetime
cadastro = dict()
Este_ano = int(str(datetime.date.today())[:4])

cadastro['nome'] = str(input('Nome: '))
cadastro['Ano_nasc'] = int(input('Ano de nascimento: '))
cadastro['ctps'] = str(input('Núm. da CTPS: '))

if cadastro['ctps'] == '0' or cadastro['ctps'] == '':
    for k, v in cadastro.items():
        print(f'{k}: {v}')
else:
    cadastro['desde'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: '))
    aposenta = Este_ano - cadastro['desde']
    cadastro['aposetadoria'] = aposenta
    for k, v in cadastro.items():
        print(f'{k}: {v}')
print('-='*20)