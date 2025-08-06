# Crie dois conjuntos: o primeiro com os valores 1, 2, 3 e 4;
# O segundo com os valores 3, 4, 5 e 6. Imprima os dois conjuntos na tela. 
# Mostre na tela o resultado das operações de união, intersecção e 
# a diferença entre os conjuntos.
# 
conj1 = {1, 2, 3, 4}
conj2 = {3, 4, 5, 6}

uniao = conj1.union(conj2)
inter = conj1.intersection(conj2)
difer = conj1.difference(conj2)
simetr = conj1.symmetric_difference(conj2)

print(f"Conjunto 1: {conj1}\nConjunto 2: {conj2}")
print("-"*30)
print(f"União: {uniao}")
print(f"Intersecção: {inter}")
print(f"Diferença: {difer}")
print(f"Diferença Simétrica: {simetr}")
print()
