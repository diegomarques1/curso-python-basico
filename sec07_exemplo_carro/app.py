class Carro:

    rodas = 4 # constante

    def __init__(self, portas, motor, teto_solar, marca, preco, tanque):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco
        self.tanque = tanque
    
    def abastecer(self, litros):
        if self.tanque >= 100:
            print("Tanque está cheio")
        else:
            self.tanque += litros
            if self.tanque > 100:
                self.tanque = 100

    def dirigir(self, km):
        km_litro = 10
        self.tanque -= (km / km_litro)

polo = Carro(4, 1.0, True, "VW", 70000, 80)
ferrari = Carro(2, 3.0, True, "Ferrari", 250000, 100)

print(polo.marca)
print(ferrari.preco)

polo.abastecer(100)
print(polo.tanque)

ferrari.dirigir(500)
print(ferrari.tanque)
ferrari.abastecer(30)
print(ferrari.tanque)