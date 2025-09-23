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