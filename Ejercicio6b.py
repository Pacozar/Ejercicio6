
class Alumno:

    nombre = None
    nota = None

    def Nombre(self, nombre):
        self.nombre = nombre
        return nombre

    def Nota(self, nota):
        self.nota = nota
        return nota

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


nombre = input('nombre alumno: ')
nota = float(input('nota alumno: '))
a = Alumno(nombre, nota)

if 5 <= nota <= 10:
    print(nombre, 'está aprobado', 'con un : ', nota)
elif nota >= 10:
    print('Nota no valida')
else:
    print(nombre, 'está suspenso', 'con un : ', nota)



