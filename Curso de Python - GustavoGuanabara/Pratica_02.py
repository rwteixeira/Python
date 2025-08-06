# Exercício para criação de Função.
# Criado em 09/01/2024, por Ricardo Wagner Teixeira.
# Ref: https://www.youtube.com/watch?v=XbvSBegg09s

produtos = ["ABC123", "abd012", " ABS111", "AbB222"]
texto = "abd012"


def tratar_texto(texto):
    texto = texto.upper()
    texto = texto.strip()
    return texto


for i, produto in enumerate(produtos):
    produtos[i] = tratar_texto(produto)

print(produtos)
