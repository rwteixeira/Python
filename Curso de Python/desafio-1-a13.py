# 1. Crie um programa que imprima os números inteiros de 10 até 1.
# Ou seja, deve-se imprimir em ordem decrescente, iniciando em 1.
# Utilize o While.
# 2. Crie um programa que continue pedindo, repetidas vezes, para que o usuário
# insira um número qualquer. O programa deve se encerrar somente quando o usuário
# inserir o valor 0 (zero).

i = 10
while i >= 1:
    print(i, " ", end="")
    i -= 1

# Programa que repete o pedido de número até o usuário digitar 0
print()

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Encerrando o programa. Até mais!")
        break
    else:
        print(f"Você digitou: {numero}")