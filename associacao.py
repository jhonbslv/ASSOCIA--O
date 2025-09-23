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