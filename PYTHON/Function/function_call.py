def greet(name,debug=False,reverse=False):#default values are entered here so its not mandatory
    if debug:
        print("Calling greet fucntion")
    if reverse:
        return f"hello {name[::-1]}"
    return name

print(greet("Sarath\n"))
print(greet("Sarath\n",debug=True))
print(greet("\nSarath",debug=True,reverse=True))