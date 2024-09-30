# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves")

# Base class: Flyer
class Flyer:
    def __init__(self, wingspan):
        self.wingspan = wingspan

    def fly(self):
        print(f"Flying with a wingspan of {self.wingspan} meters")

# Derived class: FlyingFish (inherits from both Animal and Flyer)
class FlyingFish(Animal, Flyer):
    def __init__(self, name, wingspan, fins):
        Animal.__init__(self, name)  # Initialize Animal part
        Flyer.__init__(self, wingspan)  # Initialize Flyer part
        self.fins = fins

    def swim(self):
        print(f"{self.name} can swim using {self.fins} fins")

# Create an object of FlyingFish class
flying_fish = FlyingFish("Flying Fish", 1.5, 2)

# Call methods from different classes
flying_fish.move()        # Inherited from Animal class
flying_fish.fly()         # Inherited from Flyer class
flying_fish.swim()        # Defined in FlyingFish class
