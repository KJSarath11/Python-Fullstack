######### Looping Statements #########
# its used to repeat a set of statements for any number of times. 
# 2 types:- while and for loops

########### WHILE :-##############
# is a looping statement which is used for repeating same set of statements for a specified no of times.
# syntax: 
#       while condition:
#             statement
#             updation

#hello world 5 times
i=0
while i<5 :
    print("helloworld")
    i+=1

#0-10
i=0
while i<=10:
    print(i)
    i+=1

#10 to 0
i=10
while i>=0:
    print(i)
    i-=1

#even nos from 0-20
i=0
while i<=20:
    if i%2==0:
        print(i)
    i+=1

#traversing through a string
i=0
s="hello"
while i<len(s):
    print(s[i],end='')
    i+=1

#traversing through a string backwards
i=-1
s="hello"
while i>=-len(s):
    print(s[i],end='')
    i-=1

#reversing a string
i=0
s="myworld"
rev=''
while i<len(s):
    rev=s[i]+rev
    i+=1
print(rev) 


