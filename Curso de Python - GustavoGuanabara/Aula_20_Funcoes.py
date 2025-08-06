# Aula 20: Funções - PARTE 1
# Funções são rotinas.
def mostralinha():
    print('------------------------------------')


# SERÁ EXECUTADO A PARTIR DA LINHA ABAIXO
mostralinha()


# A LINHA AMARELA NA DEF É PORQUE O PYTHON PEDE QUE HAJA
# PELO MENOS DUAS LINHAS VAZIAS DEPOIS DA DEFINIÇÃO DE FUNÇÃO.

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# PROGRAMA PRINCIPAL
soma(b=4, a=6)
soma(2, 5)
soma(123, 45)
# soma(2,6, 3) # VAI DAR ERRO!
print()
# --------------------------------------------------------
# EMPACOTAMENTO
def contador(* núm):
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 4, 8)
contador(8, 0)
contador(1,8,4,5,6,3)
# --------------------------------------------------------
print()
print('-- OUTRO EXEMPLO ---')


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

# --------------------------------------------------------
print()
print('-- OUTRO EXEMPLO ---')


def soma2(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma2(5, 2)
soma2(2, 9, 4)
