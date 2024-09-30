# n=123 #300 #20 #1
# rev=0
# temp=0
# while n>0:
#     temp=n%10#2
#     rev=rev*10+temp#32
#     n=n//10#12

# print(rev)

#PEAKK METHODD BwOIII
n=str(123)
rev=""
for i in n:
    rev+=i
print(int(rev))

