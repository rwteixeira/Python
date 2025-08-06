# COMANDO IF
nota = float(input("Digite sua nota: "))
if nota >= 4 and nota < 7:
    print("Tem direito a exame")
elif nota < 4:
    print("Reprovado")
else:
    print("Aprovado")
