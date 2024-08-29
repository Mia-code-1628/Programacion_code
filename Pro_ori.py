class animal:
    def __init__(self, idnombre, especie, tamaño, color):
        self.idnombre=idnombre
        self.especie=especie
        self.tamaño=tamaño
        self.color=color
    def mostrar(self):
        print("nombre:", self.idnombre, "especie:", self.especie,"tamaño:", self.tamaño)
animal1=animal("Tigre", "carnivoro", "grande", "marron")
animal2=animal("Gato", "carnivoro", "grande", "azul")
animal3=animal("Jirafa", "herbivoro", "grande", "amarillo y pardo")
animal4=animal("Chancho", "omnivoro", "mediano","negros" )
animal1.mostrar()
animal2.mostrar()
animal3.mostrar()
animal4.mostrar()
