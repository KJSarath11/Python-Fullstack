##1.check even
num=int(input("Enter the no :"))
if num%2==0 :
    print("The number is odd")

#2.divisible by 5 and 3
num=int(input("Enter the no :"))
if num%3==0 and num%5==0:
    print(f"{num} is true or false")

#3.checking first character is vowel or not
string=input("Enter the string: ")
if string in "aeiouAEIOU":
    print(f"{string} is starting with vowel")

#4.given string has more than 3 char or not
string=input("Enter the string: ")
if len(string)>=3:
    print("YES")

#5.given data is a list or not
# if type(data)==list:
#     print("yes")

#.isinstance(object,class_or_tuple)
data="sarath"
if isinstance(data,str):
    print("true")

#if-else:
#1.single or multi value
data=eval(input("Enter the string: "))
if isinstance(data,(int,float,complex,bool)):
    print("SVD")
else:
    print("MVD")

#1.age 18 or above eligibility
age=int(input("Enter the age: "))
if (age>=18):
    print("You are eligible.")
else:
    print("You are ineligible.")



