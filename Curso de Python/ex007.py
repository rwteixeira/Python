# Crie um programa que peça ao usuário que informe dois números.
# Calcule asoma, subtração, multiplicação e divisão desses números.
# Imprima os resultados de cada operação.

num1 = int(input("Informe o 1º número: "))
num2 = int(input("Informe o 2º número: "))

print("------------- Fase 1 -----------------")
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"Número 1: {num1}")
print(f"Número 2: {num2}")

print("------------- Fase 2 -----------------")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao:.2f}")
print()
print(f"Número 1: {num1}")
print(f"Número 2: {num2}")
print("------------- Fase 3 -----------------")
modulo1 = num1 % 2
modulo2 = num2 % 2

num1 += 1
num2 += 1

print(f"Agora o número 1 é {num1}")
print(f"Agora o número 2 é {num2}")
