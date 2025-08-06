cores = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m'}
num = int(input('\033[1;37mDigite um número inteiro: \033[m'))
print('-'*40)
print('''Escolha uma das bases para conversão:
\033[1;33m[1]\033[m \033[37mConverter para BINÁRIO\033[m
\033[1;33m[2]\033[m \033[37mConverter para OCTAL\033[m
\033[1;33m[3]\033[m \033[37mConverter para HEXADECIMAL\033[m''')
print('-'*40)
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O número {}{}{} convertido para BINÁRIO é igual a {}{}{}'.format(cores['azul'],num,cores['limpa'],cores['azul'],bin(num)[2:],cores['limpa']))
elif opcao == 2:
    print('O número {}{}{} convertido para OCTAL é igual a {}{}{}'.format(cores['azul'],num,cores['limpa'],cores['azul'],oct(num)[2:],cores['limpa']))
elif opcao == 3:
    print('O número {}{}{} convertido para HEXADECIMAL é {}{}{}'.format(cores['azul'],num,cores['limpa'],cores['azul'],hex(num)[2:],cores['limpa']))
else:
    print('\033[1;31mOpção inválida, tente novamente!\033[m')
