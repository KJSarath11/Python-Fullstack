# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves")

# Derived class: Bird
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)  # Call the base class constructor
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} can fly with a wingspan of {self.wingspan} meters")

# Create an object of Bird class
sparrow = Bird("Sparrow", 0.25)
sparrow.move()  # Inherited method
sparrow.fly()   # Bird method
