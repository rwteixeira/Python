class Carro:
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")

    def frear(self):
        self.velocidade -= 5
        print(f"{self.modelo} reduziu para {self.velocidade} km/h.")


meu_carro = Carro("Fusca", "Azul")
meu_carro.acelerar()
meu_carro.frear()


