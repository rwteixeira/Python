# ORIENTAÇÃO A OBJETO
# 
# Crie uma classe pai, chamada Animal, cujos atributos são o nome e a espécie 
# do animal, e um único método: fala(). Em seguida, crie duas subclasses derivadas
# de Animal:
#  - Cachorro: com dois atributos: nome e raça. Inicialize a espécie animal como
# 'Cachorro'. No método fala(), retorne uma string dizendo algo como 
# "<nome> é <raça> e late";
# 
#  - Gato: com os atributos nome e cor. Inicialize a espécie do animal como "Gato".
# No método fala(), retorne uma string dizendo algo como "<nome é <cor> e mia";
# 
#  - Crie dois objetos: um cão e um gato, ambos com os atributos que desejar;
#  - Imprima na tela todos os atributos de cada um dos objetos;
#  - Invoque a função fala() de cada um dos objetos e imprima o retorno na tela.
# 

class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fala(self):
        return f"{self.nome} é um(a) {self.especie}"
    
class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca
    
    def fala(self):
        return f"{super().fala()} e late"

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, "Gato")
        self.cor = cor
    
    def fala(self):
        return f"{super().fala()} e mia"

dog = Cachorro("Lord","Caramelo")
cat = Gato("Pipoca","Rajado")

print("Atributos do Cachorro:")
print(f"Nome: {dog.nome}")
print(f"Raça: {dog.raca}")
print(f"Espécie: {dog.especie}")
print(dog.fala())
print()
print("Atributos do Gato:")
print(f"Nome: {cat.nome}")
print(f"Raça: {cat.cor}")
print(f"Espécie: {cat.especie}")
print(cat.fala())
print()
