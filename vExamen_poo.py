class Empleado:
    def __init__ (self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    def mostrar_info(self):
        print(self.nombre, self.edad,self.salario)

class Gerente(Empleado):
    def __init__ (self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
    def mostrar_info(self):
        print(self.nombre, self.edad, self.salario,self.departamento)

class Ingeniro(Empleado):
    def __init__ (self, nombre, edad, salario, especialidad):
        super().__init__ (nombre, edad, salario)
        self.especialidad = especialidad
    def mostrar_info(self):
        print(self.nombre, self.edad, self.salario, self.especialidad)

gerente1 = Gerente("Emir", 25, 43000, "Ventas")
gerente1.mostrar_info()

ingeniro1 = Ingeniro("Lia", 21, 50000, "Hardware")
ingeniro1.mostrar_info()
