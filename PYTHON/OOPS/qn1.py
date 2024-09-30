#wapt create details of employee and class variable 
class Qspiders:
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal

    def details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Sal:{self.sal}")

emp1=Qspiders("Venkitesh",25,40000)
emp2=Qspiders("Gagan",26,50000)

print(emp1.name)
print(emp2.name)

print(emp1.age)
print(emp2.age)

print(emp1.sal)
print(emp2.sal)

print(emp1.details())
print(emp2.details())
        
