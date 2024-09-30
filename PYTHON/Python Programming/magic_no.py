def magic(num):
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit
        num=num//10 
    if sum>9:           
        return magic(sum)
    else:
        return sum


n=1234
sum_=magic(n)
if sum_==1:
    print("Magic No")
else:
    print("Not Magic No")
