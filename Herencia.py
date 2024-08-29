class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, matricula):
    Person.__init__(self, fname, lname)
    self.matricula=matricula
  def printname(self):
    super().printname(self)

x1 = Student("Mike", "Olsen",120)
x1.printname()