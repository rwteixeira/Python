# Crie um programa que peça para que o usuário continue informando
# números inteiros. O programa deve armazenar tais números em uma lista. O programa
# deve parar de capturar novos números caso o usuário insira 0 (zero).
# Ao final, o programa deve informar a quantidade de elementos adicionados na
# lista, bem como, o menor e o maior elemento digitado (excluindo o zero).
# By: RWT - 29/07/2025 - 17:26h
# Ref: https://www.youtube.com/watch?v=BudlaI2cwGk&list=PLpaKFn4Q4GMN1A4J1FnhW_anOGt8ug8ip&index=17
#  
lista = []
num = 0
ma = 0
me = 0
soma = 0
cont = 0

while True:
    num = int(input("Digite um valor inteiro. Para sair[0]:"))
    soma += num
    cont += 1

    if num == 0:
        break
    if cont == 1:
        ma = me = num
    else:
        if num > ma:
            ma = num
        if num < me:
            me = num
    lista.append(num)

print(lista)
print(f"A lista possui {len(lista)} elementos.")
print(f"O maior número é {ma}")
print(f"O menor número é {me}")
print(f"A somatória dos elementos é {soma} e a média é {soma / (cont - 1):.2f}")
