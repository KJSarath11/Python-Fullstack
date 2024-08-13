# 2.given string is paliandrome or not 
# reversed_string=string[::-1] need not be perfomed because string is immutable and can be displayed as its own
#string is sliced here to reverse the string.....
string=int(input("Enter a string: "))
if(string==string[::-1]): 
    print("The string is a paliandrome.")
else:
    print("The string is not a paliandrome.")

