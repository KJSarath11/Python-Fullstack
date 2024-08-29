
def func1():
    print("Func One")
    a = 1
    res = a + func2()#2 + func3()#3   #1+2+3=6
    return res

def func2():
    print("Func Two")
    a=2
    res=a+func3()
    return res

def func3():
    print("Func Three")
    a=3
    return a

print(func1())  # displays 3 functions inside
# print(func2())# displays 2 fucntions inside 
# print(func3())# display the function itself.
