# used to repeat set of instructions for n no of times
# for var_name in iterable/collection.
# range is an iterable or inbuilt or generic function which is used to generate integer nos from 0 to n-1.
# here we can pass the range.

####################### RANGE ##########################
#Range(start,end,step)
#cant pass float numbers for start end or step...
for numbers in range(0,20):
    print(numbers)

for numbers in range(0,20,5):
    print(numbers)


#10-0
for numbers in range(10,-1,-1):
    print(numbers)

#iterating through string
s="hello world"
for each_character in range(0,len(s)):
    print(s[each_character])

for each_character in s:
    print(each_character)

#reversed string(string concatenation is used to reverse the string..)
reverse=" "
for each_character in s:
    reverse+=each_character
print(reverse)

#alternative characters
for each_character in range(0,len(s),2):
    print(s[each_character])

#printing index and character:
s="hello"
for num in range(0,len(s)):
    print(num,s[num],sep="->")

##################### ENUMERATE ##########################
# inuilt or generic function which is used to fetch the charcter/item along with its index value.
# syntax: enumerate(iterable,start=0)
#it need two values to enumerate index and the character..

#printing index and character
s="hello"
for index,each_character in enumerate(s):
    print(index,each_character)


########################### ZIP ###############################
#inbuilt/generic function which is used to iterate over multiple iterables simultaneously

#iterating over mutlitiple string objects using zip class
s1="hello"
s2="world"

for char1,char2 in zip(s1,s2):
    print(char1,char2)

#appending two lists
a=[1,2,3,4,5]
b=[3,4,5,6,7]
add=[]

for num1,num2 in zip(a,b):
    add.append(num1+num2)
print(add)