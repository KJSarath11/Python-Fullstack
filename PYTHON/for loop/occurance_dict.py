#write a program to count the no of occurances of each item in the list without using count().
#dictionary used normally for count type qns..
names=["apple","google","apple","yahoo","google","facebook","gmail","yahoo"]
count={}
for item in names:
    if item not in count:
        count[item]=1 #it should be normally assigned before entering any values into dictionary
    else:
        count[item]+=1
print(count)