# Tuplas - Variáveis compostas, Listas e Dicionários.
# Rotinas e tratamento de erros. Mundo III.
# Tuplas são IMUTÁVEIS.
#
# Exemplo de tupla: lanche (tupla) [lista] {dicionário}
#
# Ref: https://www.youtube.com/watch?v=0LB3FSfjvao
#
lanche = 'Hamburger','Suco','Pizza','Pudim','Batata frita'
print(lanche[0])
print(lanche[1:3])
print(lanche[:2])
print(lanche[-3])
print(lanche[-1])
print(lanche[-3:])
print(lanche[-2:])
print(lanche)
print('-'*40)
print(len(lanche))
print('-1'*40)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-2'*40) #    2

print('-3'*40) #    3
for cont in range(0, len(lanche)):
    print(cont)
print('-4'*40) #    4
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('-5'*40) # SITUAÇÃO QUE PRECISE ENUMERAR ALGO. #  5
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('-6'*40) #    6
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('-7'*40) #    7
print((lanche)) # ORIGINAL
print(sorted(lanche)) # CLASSIFICADA
print('-8'*40) #    8
a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(len(c))
print(c.count(5))
print(c.count(4))
print(c.count(9))
print('-9'*40) #    9
print(c)
print(c.index(8))
print(c.index(4))
print(c.index(2)) # VAI MOSTRAR A 1ª POSIÇÃO
print(c.index(5))
print(c.index(5,1))
print('-10'*40) #   10
pessoa = ('Ricardo', 59, 'M', 80)
pessoa2 = ('Ricardo', 59, 'M', 80)
print(pessoa)
# del(pessoa2)
print(pessoa2)
