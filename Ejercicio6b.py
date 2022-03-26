class Alumno:

    nombre = None
    nota = None

    def anombre(self, nombre):
        print(nombre)

    def anota(self, nota):
        if 5 <= nota <= 10:
            print('esta aprobado con un', nota)
        elif nota > 10:
            print('introduce un numero del 0 al 10')
        else:
            print('esta suspenso con un', nota)

    def __init__(self, nombre, nota):
        self.anombre(nombre)
        self.anota(nota)

a = Alumno('paco', 10)