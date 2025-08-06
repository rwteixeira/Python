import random
n1 = random.randint(0,5)
n2 = int(input('Tente advinhar o número do computador entre 0 e 5: '))
print('-'*40)
print('O número do jogado pelo computador foi {}'.format(n1))
print('Seu número foi {}'.format(n2))
if n1 == n2:
    print('PARABÉNS!, você acertou!')
else:
    print('ERROU!, tente mais uma vez!')
