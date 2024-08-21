def greet(name,debug=False,reverse=False):#default values are entered here so its not mandatory
    if debug:
        print("Calling greet fucntion")
    if reverse:
        return f"hello {name[::-1]}"
    return name

print(greet("Sarath\n"))
print(greet("Sarath\n",debug=True))
print(greet("\nSarath",debug=True,reverse=True))

#Calculator
# rather than doing it in a if-elif way we are trying it with dictionary and fucntion combination.
# here the behaviour of fucntion is taught.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b

functions={
    1:add,
    2:sub,
    3:mul
}

def calculator(opcode,a,b):
    if opcode in [1,2,3]:
       return functions[opcode](a,b)
    return "UNKNOWN OPN"