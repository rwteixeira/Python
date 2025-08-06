# Fluxo Interno [21/12/2024] - Enseada/SC
# Internamente, o enumerate funciona como uma espécie de gerador:
# Cria um par (índice, valor) a cada chamada.
# Economiza memória porque os pares são gerados sob demanda.

valores = [5,3,9]
#valores = ["x", "y", "z"]
enumerator = enumerate(valores)

#print(next(enumerator))  # (0, 'x')
#print(next(enumerator))  # (1, 'y')
#print(next(enumerator))  # (2, 'z')

cont = len(valores)

for i in range(1, cont + 1):
    print((next(enumerator)))
