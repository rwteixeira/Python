# Desenvolva um programa que leia o nome, idade e o sexo de 4 pessoas.
# No final do programa mostre:
# 1) A média de idade do grupo. 2) Qual é o nome do homem mais velho.
# 3) quantas mulheres tem menos de 20 anos.
# Esse código não é do RWT.
somaidade = 0
nomehomem = ''
maioridadehomem = 0
mulheresmenos20 = 0
for p in range(1,5):
    print('---------- {}ª PESSOA ----------'.format(p))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    media = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomem = nome
    if sexo in 'Ff' and idade < 20:
        mulheresmenos20 += 1

print('A média de idade do grupo é de {} anos.'.format(media))
print('A idade do homem mais velho é {} anos e ele se chama {}.'.format(maioridadehomem,nomehomem))
print('No total são {} mulheres com menos de 20 anos.'.format(mulheresmenos20))
