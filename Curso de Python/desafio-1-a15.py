# Crie um programa que mostre, na tela, um contador. O contador
# deve ser inicializado com zero. O usuário deve ter a opção deincrementar
# uma unidade ao contador, ou de emcerrar o programa. Enquanto o usuário continuar
# decidindo incrementar o contador, o programa não deve ser encerrado. O programa encerra
# somente quando o usuário decidir. Utilize um laço com os comandos Continue e Break.

i = 0

while True:
    res = str(input("Deseja continuar? [S/N] "))
    if res in "Ss":
        print(i)
        i += 1
        continue
    else:
        if res in "Nn":
            print("O programa foi interrompido!")
            break
    
    

