#list method
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
numbers = sorted([num1, num2, num3])
print("The second largest number is:", numbers[1])

#if-elif-nested if method
a = int(input("Enter the first no: "))
b = int(input("Enter the second no: "))
c = int(input("Enter the third no: "))
if a>=b and a>=c:#b<=a>=c
    if b > c:
        print("The second largest number is:", b)
    else:
        print("The second largest number is:", c)
elif b>=c and b>= a:
    if a > c:
        print("The second largest number is:", a)
    else:
        print("The second largest number is:", c)
else:
    if a >= b:
        print("The second largest number is:", a)
    else:
        print("The second largest number is:", b)

