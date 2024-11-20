class Classroom:
    def __init__(self,name):
        self.name=name
    def meth(self):
        print(f"{self.name} is a good boy")

class Classroom_(Classroom):
    def __init__(self, name,mark):
        super().__init__(name)
        self.mark=mark 
    def meth(self):
        print(f"{self.name} is a good boy with {self.mark} marks")

sarath=Classroom_("sarath",90)
sarath.meth()