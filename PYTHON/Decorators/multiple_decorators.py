##### Multiple Decorators #####
def positive(func):
    #outer fucntion-decorator.takes m/y address of callback and returns m/y address of inner fucntion(wrapper)
    def wrapper(*args): 
        res= func(*args)   
        if isinstance(res,(int,float)): #not mandatory to check the instance
            return abs(res)#absolute
    return wrapper

from time import sleep
def delay(func):
    #outer fucntion-decorator.takes m/y address of callback and returns m/y address of inner fucntion(wrapper)
    def wrapper(*args): 
        #inner function-takes args of the callback fucntion.we also invokes 'call back' by passing required args.also pass the 'extra-functionalities'.
        sleep(2)    #extra-fucntionality/decorator
        return func(*args)  #invoking call back
    return wrapper

from time import time
def measure_time(func):
    def wrapper(*args):
        start_time=time()
        # print(start_time)
        result=func(*args)
        end_time=time()
        # print(end_time)
        print(f"total execution time taken by {func.__name__} function : {end_time-start_time}")
        return result
    return wrapper

def log(func):
    def wrapper(*args):
        print(f"you called {func.__name__} function")
        return func(*args)
    return wrapper

@log #it calls the delay fn by pass memory address of wrapper(here greet..)
def greet():#inner fucntion calls the fucntion...
    return "helllo world"

@log
def greeting(name):
    return f"hello {name}"

@positive
@delay
@measure_time
def add(a,b):
    sleep(2)
    return a+b

@log
def sub(a,b,c):
    sleep(3)
    return a-b-c

# print(add(3,4))
# print(sub(8,4,2))
print(greet())