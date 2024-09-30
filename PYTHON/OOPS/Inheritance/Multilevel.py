# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves")

# Derived class: Bird
class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} can fly with a wingspan of {self.wingspan} meters")

# Derived class: Parrot (inherits from Bird)
class Parrot(Bird):
    def __init__(self, name, wingspan, color):
        super().__init__(name, wingspan)  # Initialize Bird part
        self.color = color

    def talk(self):
        print(f"{self.name} is a {self.color} parrot that can talk!")

# Create an object of Parrot class
parrot = Parrot("Polly", 0.5, "green")
parrot.move()  # Inherited method from Animal
parrot.fly()   # Inherited method from Bird
parrot.talk()  # Parrot method
