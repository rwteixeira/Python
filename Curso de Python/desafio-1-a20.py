# Crie um programa  com dois conjuntos (sets) de strings.
# O primeiro conjunto deve ser inicializado com os nomes das seguintes
# pessoas: Ricardo, Roberto, Robinson e Lucia.
# O segundo grupo, deve ser: Ana, Lucia, Lisa e Ricardo
# Assim sendo, descubra:
#  - Quais são as pessoas que estão presentes nos dois grupos?
#  - Quais são as pessoas que estão apenas em um grupo?
#  - Liste todas as pessoas mencionadas no enunciado, sem repetir seus nomes.

g1 = {"Ricardo","Roberto","Robinson","Lucia"}
g2 = {"Ana","Lucia","Lisa","Ricardo"}
g3 = {"Arthur","Samuel","Roberto","Ricardo"}
g4 = {"Lilo","Lady","Lord","Lobão","Roberto"}

inter = g1.intersection(g2)
uniao = g1.union(g2)
difer = g1.symmetric_difference(g2)

inter2 = g1.intersection(g3)
inter3 = inter2.intersection(g4)

print(g4)
excluir = str(input("Excluir quem: "))
g4.discard(excluir)
print(g4)

print(f"Pessoas que aparecem nos dois grupos: {inter}")
print(f"Pessoas que aparecem somente em um dos grupos: {difer}")
print(f"Pessoas de todos os grupos: {uniao}")
print(f"Número total de pessoas [sem repetição]: {len(uniao)}")

print(inter3)
adicionar = str(input("Adicionar no G4: "))
g4.add(adicionar)
print(g4)
