class Alumno:
    def __init__ (self, nombre, nota, resultado):
        self.nombre=nombre
        self.nota=nota
        self.resultado=resultado
    def mostrar(self):
        print ("Nombre:", self.nombre, "Nota:", self.nota, "Resultado", self.resultado)  
    
alumno1:Alumno("Angela", 7, "Aprobado")
alumno2:Alumno("Hector", 9, "Aprobado")
alumno3:Alumno("Fiorela", 3, "Reprobado")
alumno1.mostrar()
alumno2.mostrar()
alumno3.mostrar()