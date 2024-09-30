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

# Derived class: Fish
class Fish(Animal):
    def __init__(self, name, fins):
        super().__init__(name)  # Call the base class constructor
        self.fins = fins

    def swim(self):
        print(f"{self.name} can swim using {self.fins} fins")

# Derived class: Reptile
class Reptile(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)  # Call the base class constructor
        self.scale_color = scale_color

    def crawl(self):
        print(f"{self.name} crawls and has {self.scale_color} scales.")

# Create objects of derived classes
sparrow = Bird("Sparrow", 0.25)
goldfish = Fish("Goldfish", 5)
lizard = Reptile("Lizard", "green")

# Call methods from different classes
sparrow.move()       # Inherited from Animal class
sparrow.fly()        # Bird method

goldfish.move()      # Inherited from Animal class
goldfish.swim()      # Fish method

lizard.move()        # Inherited from Animal class
lizard.crawl()       # Reptile method
