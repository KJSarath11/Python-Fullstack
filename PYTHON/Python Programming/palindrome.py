n=121 
rev=0
temp=0
while n>0:
    temp=n%10#2
    rev=rev*10+temp#32
    n=n//10#12
print(rev)
if rev==n:
    print("P")
else:
    print("NP")