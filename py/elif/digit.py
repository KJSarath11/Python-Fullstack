num=int(input("Enter the number: "))

if 0<=num<=9:
    print("Single")
elif 10<=num<=99:
    print("Two")
elif 100<=num<=999:
    print("Three digit")
else:
    print("More than 3")