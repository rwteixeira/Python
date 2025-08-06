tupla = (0,1,3,3,5,7,7,7)

while True:
    pesq = int(input("Pesquisar: "))
    if pesq != 999:
        if pesq in tupla:
            print(f"Ocorrências: {tupla.count(pesq)}")
            print(f"Primeira posição: {tupla.index(pesq)}")
            print(f"Quantidade de elementos: {len(tupla)}")
            sn = input("Pesquisar posição? [S/N] ").upper()
            if sn in "S":
                pos = int(input("Pesquisar posição: "))
                print(tupla[pos])
        else:
            print("Valor inválido!")
            continue
    else:
        print("Deixando o programa!")
        break

