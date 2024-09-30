class student:
    institute="Pyspiders Kochi"#class variable
    def __init__(self,name,age,phno,addr):
        self.name=name
        self.age=age
        self.phno=phno
        self.addr=addr
    
    def details(self):
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Phno:{self.phno}")
        print(f"Address:{self.addr}")

#object created here
s1=student("Sarath",22,949691270,"Ashtamichira")

#fetching class variable using class name
print(student.institute)#Pyspiders Kochi

#fetching class variable using object reference
print(s1.institute)#Pyspiders Kochi

#instance variable using class names
#print(student.name)    #AttributeError: type object 'student' has no attribute 'name'

#instance variable using object reference
print(s1.name)

#fetch details using class
#print(student.details())    #TypeError: student.details() missing 1 required positional argument: 'self

#fetch details using object
print(s1.details())



