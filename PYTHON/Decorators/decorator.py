#1.Giving the extra-functionality _SLEEP_ inside a function call
# from time import sleep

# def delay(func):
#     #outer fucntion-decorator.takes m/y address of callback and returns m/y address of inner fucntion(wrapper)
#     def wrapper(*args): 
#         #inner function-takes args of the callback fucntion.we also invokes 'call back' by passing required args.also pass the 'extra-functionalities'.
#         sleep(2)#extra-fucntionality/decorator
#         return func(*args)  #invoking call back
#     return wrapper

# @delay #it calls the delay fn by pass memory address of wrapper(here greet..)
# def greet():#inner fucntion calls the fucntion...
#     return "helllo world"

# @delay
# def greeting(name):
#     return f"hello {name}"

# @delay
# def add(a,b):
#     return a+b

# @delay
# def sub(a,b,c):
#     return a-b-c

# print(add(3,4))

#2.Giving the extra-functionality _ABS_ inside a function call

# def positive(func):
#     #outer fucntion-decorator.takes m/y address of callback and returns m/y address of inner fucntion(wrapper)
#     def wrapper(*args): 
#         res= func(*args)   
#         if isinstance(res,(int,float)): #not mandatory to check the instance
#             return abs(res)#absolute
#     return wrapper

# @positive #it calls the positive fn by pass memory address of wrapper(here greet..)
# def greet():#inner fucntion calls the fucntion...
#     return "helllo world"

# @positive
# def greeting(name):
#     return f"hello {name}"

# @positive
# def add(a,b):
#     return a+b

# @positive
# def sub(a,b,c):
#     return a-b-c

# print(sub(3,4,2))

