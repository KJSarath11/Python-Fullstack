from time import sleep


def delay(func):
    # outer fucntion-decorator.takes m/y address of callback and returns m/y address of inner fucntion(wrapper)
    def wrapper(*args):
        # inner function-takes args of the callback fucntion.we also invokes 'call back' by passing required args.also pass the 'extra-functionalities'.
        sleep(2)  # extra-fucntionality/decorator
        return func(*args)  # invoking call back

    return wrapper


def greet():
    return "helllo world"


def greeting(name):
    return f"hello {name}"


def add(a, b):
    return a + b


def sub(a, b, c):
    return a - b - c


def spam(something, *args):
    return something(*args)


# print(spam(greet))
# print(spam(greeting,"Sarath"))
# print(spam(add,1,2))
# print(spam(sub,15,4,3))
res = delay(add)
res1 = delay(greet)
res2 = delay(greeting)
res3 = delay(sub)
print(res)
print(res.__name__)
print(res(3, 4))
