class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def mostrar(self):
     print(self.name,self.age)


p1 = Person("Mia", 16)#OBJETO DE LA CLASE Person
p1.mostrar()
