# MUTABILIDADE E IMUTABILIDADE
variavel_numerica = 5

print("Variável numérica (antes da alteração):")
print("Conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))

variavel_numerica = 10

print("Variável numérica (depois da alteração):")
print("Conteúdo:", variavel_numerica)
print("ID:", id(variavel_numerica))

lista_mutavel = [10, 20, 30]

print("Variável numérica (antes da alteração):")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))

lista_mutavel.append(40)
lista_mutavel[0] = 0

print("Variável numérica (depois da alteração):")
print("Conteúdo:", lista_mutavel)
print("ID:", id(lista_mutavel))
