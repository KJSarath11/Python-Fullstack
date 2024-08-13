l=[50,90.5,"hello","bye",13]
sum=0
i=0
while i<len(l):
    if isinstance(l[i],(int,float)):
        sum+=l[i]
    i+=1
print(sum)