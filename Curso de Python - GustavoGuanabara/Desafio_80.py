# Desafio_80: Crie um programa onde o usuário possa digitar cinco valores
# numéricos e cadastrá-los em uma lista, já na posição correta de inserção
# (sem usar sort()). No final, mostre a lista ordenada na tela.
lista = list()
ult_valor = 0
for i in range(0,5):
    n = int(input('Digite um valor: '))
    if i == 0 or n > lista[-1]: # list[len(lista)-1] Se for maior que o último valor.
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posiçao {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
