def factorial(n:int)->int:
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print(factorial(5))   # Output: 120 
print(factorial(0))   # Output: 1
print(factorial(7))   # Output: 5040
