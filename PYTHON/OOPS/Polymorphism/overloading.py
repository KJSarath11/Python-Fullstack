class one:
    def __init__(self):
        self.c=1
    def meth(self,*args):
        print(f"Funtion call count:{self.c}")
        print(args) 
        self.c+=1

obj=one()
obj.meth(10,20,30,40)
obj.meth(10)
