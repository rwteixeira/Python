# FUNÇÕES - EXEMPLOS:
# 1. Crie um programa para definir e executar uma função que
# recebe dois números como parâmetro e retorna o maior entre
# os dois números.
 

def encontra_maior(a, b):
    if a > b:
        return a
    else:
        return b

n1 = int(input("Digite 1ª entrada: "))
n2 = int(input("Digite 2ª entrada: "))

res = encontra_maior(n1, n2)

print(f"A entrada maior é: {res}")
