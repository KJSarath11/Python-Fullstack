def is_prime(n:int)->bool:
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0:
        return False
    
    for i in range(3,int(n**0.5)+1,2):#? n**0.5 determines the no of loops performed
        if n%i==0:
            return False
    return True

print(is_prime(2))    # Output: True
print(is_prime(17))   # Output: True
print(is_prime(20))   # Output: False
