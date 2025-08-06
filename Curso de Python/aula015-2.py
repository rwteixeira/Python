# Crie um programa com um laço que itere por 10 vezes, imprimindo os valores na tela.
# Dentro do laço, adicione uma condição para que, caso estejamos na quinta iteração,
# o comando break force o laço a interrompera sua execução por completo.
#
faixa = int(input("Informe a faixa: "))
ponto = int(input("Ponto de parada: "))

if ponto > faixa:
    print("Valor inválido!")

for i in range(1, faixa + 1):
    if i == ponto:
        break
    print(i, " ", end="")