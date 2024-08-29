class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        print(self.marca, self.modelo, self.ano)

class Auto(Vehiculo):
    def __init__(self, marca, modelo, ano, color):
        super().__init__(marca, modelo, ano)
        self.color = color
    def mostrar_info(self):
        print(self.marca,self.modelo,self.ano,self.color)
    

class Moto(Vehiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo
    def mostrar_info(self):
        print(self.marca,self.modelo,self.ano,self.tipo)
        

class Camion(Vehiculo):
    def __init__(self, marca, modelo, ano, capacidad_carga):
        super().__init__(marca, modelo, ano)
        self.capacidad_carga = capacidad_carga
    def mostrar_info(self):
        print(self.marca,self.modelo,self.ano,self.capacidad_carga)
        

    
auto1 = Auto("Lamborghini", "HURACÁN EVO SPYDER", 2020,"Verde")
moto1 = Moto("Yamaha", "R15", 2008, "Deportiva")
camion1 = Camion("Volvo Group", "C40 Recharge", 2021, 1205)

auto1.mostrar_info()
print()
moto1.mostrar_info()
print()
camion1.mostrar_info()
print()
