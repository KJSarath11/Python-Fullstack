def s_palindrome(s:str)->bool:
    s=s.lower()
    return s==s[::-1]

def n_palindrome(n:int)->bool:
    s=str(n)
    return s==s[::-1]

print(s_palindrome("malayalam"))
print(n_palindrome(121))
print(s_palindrome("true"))
print(n_palindrome(123))

#! Number Palindrom without converting it into string
def pali(n:int)->bool:
    if n<0:
        return False
    
    original_no=n
    reversed_no=0
    while n>0:
        reversed_no=reversed_no*10+n%10
        n=n//10
    return original_no==reversed_no

print(pali(121))    # Output: True
print(pali(12321))  # Output: True
print(pali(123))    # Output: False

