class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre: {self.nombre}")
        print("Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 7:
            print("El alumno {self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print("El alumno {self.nombre} ha desaprobado con una nota de {self.nota}.")

alumno1 = Alumno("Antonio Pérez", 9)
alumno2 = Alumno("Martina Gómez", 5)

alumno1.imprimir_datos()
alumno1.resultado()

alumno2.imprimir_datos()
alumno2.resultado()