# Interrompendo repetições While
# fstrings python 3
n = s = 0
while True:
    n = int(input('digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')
# Exemplo
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}.') # PYTHON 3.6+
print('O {} tem {} anos e ganha R${:.2f}.'.format(nome, idade, salario)) # PYTHON 3
print('O %s tem %d anos.'%(nome, idade)) # PYTHON 2
