# Desafio_76: crie um programa que tenha uma tupla única com
# nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os
# dados em forma tabular.
# Ref: https://www.youtube.com/watch?v=Qp2cXfCHk2I
listagem = ('Cerveja importada (330 ml)',12.20,
            'Cerveja nacional (0,5 litros)',6.20,
            'Garrafa de vinho qual. média',40.10,
            'Água (garrafa de 1,5 litros)',3.40,
            'Alface (1 unidade)',3.50,
            'Cebolas (1kg)',5.10,
            'Batatas (1 kg)',5.30,
            'Tomates (1 kg)',7.80,
            'Laranjas (1kg)',4.7,
            'Bananas (1kg)',5.70,
            'Maçãs (1 kg)',8.80,
            'Queijo fresco (1 kg)',44.00,
            'Uma dúzia de ovos',10.30,
            'Arroz (1 kg)',5.80,
            'Um quilo de pão (1 kg)',7.50,
            'Leite (1 litro)',5.30)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-'*40)