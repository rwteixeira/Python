# Crie um dicionário para representar os dados de uma pessoa
# que possui nome, idade e peso. Crie uma pessoa cujos dados
# são "Teste" para o nome, 0.0 para o peso e 0 para a idade.
# Imprima os dados da pessoa na tela. Em seguida, altere  os
# dados para "Texto", 99.99 e 10, para os  mesmos dados res-
# pectivos. Imprima novamente. Por fim, peça ao usuário  que
# informe o nome, o peso e a idade  desta mesma pessoa e im-
# prima os dados na tela.
# 
# nome, idade, peso
pessoa = {
    "nome": "Teste",
    "peso": 0.0,
    "idade": 0
}

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])
print()

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])
print()

pessoa["nome"] = input("Digite seu nome: ").capitalize()
pessoa["peso"] = float(input("Digite seu peso: "))
pessoa["idade"] = int(input("Digite sua idade: "))
print()
print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])
print()