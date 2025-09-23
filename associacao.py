class Motor:
    def __init__(self, potencia, marca_motor):
        self.potencia = potencia
        self.marca_motor = marca_motor

    def get_potencia(self):
        return self.potencia