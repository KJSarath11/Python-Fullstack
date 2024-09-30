# Base class: 
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} moves")

# Derived class: Bird (adds wingspan attribute)
class Bird(Animal):
    def __init__(self, name, wingspan):
        Animal.__init__(self, name)  # Call the base class constructor
     #here we are calling animal.__init__ because its  multiple inheritance which is followed here
        self.wingspan = wingspan
   
    def fly(self):
        print(f"{self.name} can fly with a wingspan of {self.wingspan} meters")

# Derived class: Fish (adds fins attribute)
class Fish(Animal):
    def __init__(self, name, fins):
        Animal.__init__(self, name)  # Call the base class constructor
    #here we are calling animal.__init__ because its  multiple inheritance which is followed here
        self.fins = fins

    def swim(self):
        print(f"{self.name} can swim using {self.fins} fins")

# Derived class: FlyingFish (inherits from Bird and Fish)
class FlyingFish(Bird, Fish):
    def __init__(self, name, wingspan, fins):
        Bird.__init__(self, name, wingspan)  # Initialize Bird part
        Fish.__init__(self, name, fins)      # Initialize Fish part
    #here we are calling bird.__init__ and fish.__init__ because its  multiple inheritance which is followed here

    def special_ability(self):
        print(f"{self.name} can fly and swim")

# Create an object of FlyingFish class
flying_fish = FlyingFish("Flying Fish", 1.5, 2)

# Call methods from different classes
flying_fish.move()           # Inherited from Animal class
flying_fish.fly()            # Inherited from Bird class
flying_fish.swim()           # Inherited from Fish class
flying_fish.special_ability()  # Defined in FlyingFish class