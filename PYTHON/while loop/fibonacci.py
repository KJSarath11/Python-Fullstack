a=0
b=1
count=1
n=int(input("Enter the no: "))
print(a,end=" ")
while(count<n):
    print(b,end=" ")
    c=a+b
    a=b
    b=c
    count+=1


