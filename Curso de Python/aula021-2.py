# Modele um dicionário para representar os dados de uma
# pessia que possui nome, idade e peso. Crie uma lista que
# seja capaz de armazenar os dados de três pessoas distintas.
# Peça para que o usuário informe todos os dados de todas as
# pessoas. Imprima os dados informados na tela.
# 
lista_pessoas = []

for _ in range(3):
    pessoa = {}
    pessoa["nome"] = input("Digite seu nome: ").upper()
    pessoa["peso"] = float(input("Digite seu peso: "))
    pessoa["idade"] = int(input("Digite sua idade: "))
    lista_pessoas.append(pessoa)

print("Dados das pessoas:")
for pessoa in lista_pessoas:
    print()
    print("Nome:", pessoa["nome"])
    print("Peso:", pessoa["peso"])
    print("Idade:", pessoa["idade"])
