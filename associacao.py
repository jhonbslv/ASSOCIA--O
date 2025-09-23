class Motor:
    def __init__(self, potencia, marca_motor):
        self.potencia = potencia
        self.marca_motor = marca_motor

    def get_potencia(self):
        return self.potencia
    
    def get_marca_motor(self):
        return self.marca_motor
    
class Roda:
    def __init__(self, tamanho_roda, marca_roda):
        self.tamanho_roda = tamanho_roda
        self.marca_roda = marca_roda

    def get_tamanho_roda(self):
        return self.tamanho_roda

    def get_marca_roda(self):
        return self.marca_roda
    
class Carro:
    def __init__(self):
        self.motor = None
        self.rodas = []

    def set_motor(self, motor):
        self.motor = motor

    def set_rodas(self, rodas):
        self.rodas = rodas

    def get_motor(self):
        return self.motor 

    def get_rodas(self):
        return self.rodas
    
motor1 = Motor(2.0, "Ford")
motor2 = Motor(1.6, "Volkswagen")
motor3 = Motor(3.0, "BMW")

roda1 = Roda(17, "Pirelli")
roda2 = Roda(18, "Michelin")

carro1 = Carro()
carro2 = Carro()
carro3 = Carro()
carro4 = Carro()
carro5 = Carro()
carro6 = Carro()

carro1.set_motor(motor1)
carro1.set_rodas([roda1, roda1, roda1, roda1])

carro2.set_motor(motor1)
carro2.set_rodas([roda2, roda2, roda2, roda2])

carro3.set_motor(motor2)
carro3.set_rodas([roda1, roda1, roda1, roda1])

carro4.set_motor(motor2)
carro4.set_rodas([roda2, roda2, roda2, roda2])

carro5.set_motor(motor3)
carro5.set_rodas([roda1, roda1, roda1, roda1])

carro6.set_motor(motor3)
carro6.set_rodas([roda2, roda2, roda2, roda2])