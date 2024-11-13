def fibonacci(n:int)->list:
    if n<=0:
        return []
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    
    fib_seq=[0,1]
    for i in range(2,n):
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    return fib_seq

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(0))
    