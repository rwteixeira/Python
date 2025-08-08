class Animal:
    def __init__(self, nome, especie):
        self.nome = nome # Atributo
        self.especie = especie # Atributo

    def descrever(self): # Método
        especie_formatada = self.especie.lower()
        return f"Este é um {especie_formatada}, chamado {self.nome}."
    
animal = Animal("Rex", "Cão") # Objeto

print(animal.descrever())
        