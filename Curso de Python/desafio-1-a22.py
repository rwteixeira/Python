# Crie um programa para simular uma calculadora. O programa deve
# ter quatro funções que sejam capazes de processar a soma, subtração,
# multiplicação e divisão entre dois números. Crie um menu de opções
# para que o usuário possa escolher qual operação matemática deseja executar.

cor = {'limpa':'\033[m',
         'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'magenta':'\033[35m',
         'ciano':'\033[36m'}

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "\033[31mErro: Divisão por zero!\033[m"
    return a / b

def menu():
    print("\n======= CALCULADORA =======")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print()

while True:
    menu()
    opcao = input("Escolha uma opção (1 - 5): ")

    if opcao == "5":
        print("Encerrando a calculadora. Até mais!")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print(f"{cor['amarelo']}Por favor, digite apenas números válidos!{cor['limpa']}")
        continue
    
    if opcao == "1":
        print(f"{cor['azul']}Resultado: {cor['limpa']}{cor['amarelo']}{somar(num1, num2)}{cor['limpa']}")
    elif opcao == "2":
        print(f"{cor['azul']}Resultado: {cor['limpa']}{cor['amarelo']}{subtrair(num1, num2)}{cor['limpa']}")
    elif opcao == "3":
        print(f"{cor['azul']}Resultado: {cor['limpa']}{cor['amarelo']}{multiplicar(num1, num2)}{cor['limpa']}")
    elif opcao == "4":
        print(f"{cor['azul']}Resultado: {cor['limpa']}{cor['amarelo']}{dividir(num1, num2)}{cor['limpa']}")
    else:
        print(f"{cor['vermelho']}Opção inválida! Tente novamente.{cor['limpa']}")


