# Desafio_77: Crie um programa que tenha uma Tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
# Ref: https://www.youtube.com/watch?v=8BgSqrOpKvU
palavras = ('aprender','lista','rota','oculos','gratis','programador','futuro','ricardo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[32m',letra,'\033[m', end=' ')
