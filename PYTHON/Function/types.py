# def func(name,age,pay):
#     return(f"{name},{age},{pay}")

# data=["steve",23,1000]
# print(func(*data))

#7.variable no of pa(*args)
# def add(*args):
#     print(args)#just displaying what parameter we given
#     total=0
#     for num in args:
#         total+=num
#     return total

# print(add(1,2,3,4))

#8.variable no of kwa(**kwargs)
def func(**kwargs):
    return(kwargs)

print(func(a=30,b=40,c=35))

#9.combination of *args and **kwargs
def func(*args,**kwargs):
    print(args)
    print(kwargs)

print(func(10,20,a=30,b=40))


    

    