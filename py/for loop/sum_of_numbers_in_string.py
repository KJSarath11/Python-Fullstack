#sum of all the numbers in the below string..
s="Sony123India567pvt2ltd"
sum=0
for char in s:
    if char.isdigit():
        sum+=int(char)
print(sum)