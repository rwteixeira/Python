# Crie um programa com um laço que itere por 10 vezes, imprimindo os
# valores na tela. Dentro do laço, adicione uma condição para que, caso estejamos
# na quinta iteração, o comando continue force o laço a interromper a iteração e saltar
# para a próxima iteração.

for i in range(1, 11):
    if i == 5:
        continue
    print(i, " ", end="")