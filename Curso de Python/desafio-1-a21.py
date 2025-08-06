# Modele um dicionário que seja capaz de armazenar os dados de um produto,
# a saber: um número de identificação (id), o nome do produto e o seu preço.
#  - Faça com que o usuário seja capaz de adicionar produtos (no máximo 5).
#   A cada inserção, deve-se imprimir na tela, a quantidade de produtos já
#   cadastrados, bem como, o id, nome e preço de cada produto.
# 
lista_produtos = []


for _ in range(2):
    produto = {}
    produto["id"] = int(input("Id: "))
    produto["produto"] = str(input("Produto: "))
    produto["preco"] = float(input("Preço: "))
    lista_produtos.append(produto)
    print(f"Você já inseriu {len(lista_produtos)} produto(s)")

print()
print("Lista de Produtos")
print("-"*20)
for produto in lista_produtos:
    print(f"Id: {produto["id"]}")
    print(f"Produto: {produto["produto"]}")
    print(f"Preço: R$ {produto["preco"]:.2f}")

print(lista_produtos)
