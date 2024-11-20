def armstrong(n:int)->bool:
    num_digits=len(str(n))#3
    sum_of_power=0
    temp=n

    while temp>0:
        digits=temp%10
        sum_of_power+=digits**num_digits
        temp//=10
    return n==sum_of_power

print(armstrong(153))   # Output: True
print(armstrong(9474))  # Output: True
print(armstrong(123))   # Output: False

