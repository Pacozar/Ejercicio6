class Alumno:

    nombre = None
    nota = None

    def obtenernombre(self, nombre):
        print(nombre)

    def obtenernota(self, nota):
        if 5 <= nota <= 10:
            print('esta aprobado con un', nota)
        elif nota > 10:
            print('introduce un numero del 0 al 10')
        else:
            print('esta suspenso con un', nota)

    def __init__(self, nombre, nota):
        self.obtenernombre(nombre)
        self.obtenernota(nota)

alumno1 = Alumno('paco', 10)
alumno1.obtenernombre('paco')
alumno1.obtenernota(6)