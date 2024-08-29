class Molde:
    def __init__(self, idmolde, alto, diametro, forma):
        self.idmolde=idmolde
        self.alto=alto
        self.diametro=diametro
        self.forma=forma
    def mostrar(self):
            print("Idmolde:", self.idmolde, "Alto:", self.alto,"Diametro:", self.diametro, "Forma:", self.forma )
    molde1=Molde(1,25,20, "Circular")
    molde2=Molde(2,35,30, "Circular")
    molde1.mostrar
    molde2.mostrar