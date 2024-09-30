n=49
no_=49
sum=0
prod=1
while(n>0):
    temp=n%10
    sum+=temp
    prod*=temp
    n=n//10

if sum+prod==no_:
    print("Its Yes")
else:
    print("its not")