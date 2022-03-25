class Vehiculo:

    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    velocidad = None
    cilindrada = None

    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


Ford = Coche('rojo', 4, 5, 123, 2323)
print('color', Ford.color)
print('ruedas', Ford.ruedas)
print('puertas', Ford.puertas)
print('velocidad', Ford.velocidad)
print('cilindrada', Ford.cilindrada)


