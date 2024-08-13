#wap to convert all the charn into uppercase if the len of that is even,if it is a odd len
# then convert it into lowercase from homogeneous list
var=['python','heLLo','worLD','king']
odd_even=[]
for item in var:
    if len(item)%2==0:#expr1
        odd_even.append(item.upper())
    else:#expr2
        odd_even.append(item.lower())
print(odd_even)

#comprehension
odd_even_=[item.upper() if len%2==0 else item.lower() for item in var]


#1. [exp for iten in iterable]
#2.[exp for item in iterable if condition]
#3.[exp1 if condition else exp2 for item in iterable]





