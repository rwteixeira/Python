# Crie um programa que leia o nome de uma cidade e diga se ela
# começa ou não com o nome 'Santo'.
cidade = input('Digite o nome de uma cidade: ')
div_cidade = cidade.split()
verificador = 'Santo'
analise = verificador.title() in div_cidade[0].title()
print('-'*40)
print('Para a cidade de {}\nA resposta é {}'.format(cidade.strip().title(),analise))
print('-'*40)