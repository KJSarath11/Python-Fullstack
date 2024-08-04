mark1=int(input("Enter the mark 1: "))
mark2=int(input("Enter the mark 2: "))
mark3=int(input("Enter the mark 3: "))
mark4=int(input("Enter the mark 4: "))
percentage=(mark1+mark2+mark3+mark4)/4
print(f"{percentage}")

if 100>=percentage>90:
    print("Distinction.")
elif 90>=percentage>75:
    print("First Class")
elif 75>=percentage>50:
    print("Second Class")
else:
    print("Fail")


