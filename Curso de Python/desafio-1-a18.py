# Concatene as palávras digitadas, 
# separando-as por espaços. Quando o usuário digitar '/exit',
# o programa deve parar de receber entradas. O termo '/exit'
# não deve ser concatenado ao resultado.
# Exiba o resultado ao final de forma ordenada alfabeticamente.
# RESOLVIDO: RWT (04/08/2025)

frase = []

while True:
    palavra = str(input("Palavra: " )).strip()
    if palavra != "/exit":
        frase.append(palavra)
    else:
        break
tamanho = len(frase)
frase.sort()
for i in range(tamanho):
    print(frase[i], end=" ")
print(f"\nA lista possui {tamanho} intens!")
print("-="*10)

