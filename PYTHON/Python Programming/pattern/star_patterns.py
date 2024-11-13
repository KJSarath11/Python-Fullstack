# for row in range(1,6):
#     for space1 in range((5-row)):
#         print(" ",end=" ")
#     for stars in range(row):
#         print("*",end=" ")
#     print()

'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

# for row in range(1,6):
#     for space in range((5-row)):
#         print(" ",end="")
#     for stars in range(row):
#         print("*",end=" ")
#     print()

'''
    *
   * *
  * * *
 * * * *
* * * * * 
'''

# for row in range(5,0,-1):
#     for space in range(row-5):
#         print(" ",end="")
#     for stars in range(row):
#         print("*",end=" ")
#     print()

'''
* * * * *
* * * *
* * *
* *
*         '''

# for row in range(5,0,-1):
#     for space in range(5-row):
#         print(" ",end="")
#     for stars in range(row):
#         print("*",end=" ")
#     print()

'''
* * * * *       
 * * * * 
  * * *
   * *
    *      '''

# for row in range(1,6):
#     for space in range((5-row)):
#         print(" ",end="")
#     for stars in range(row):
#         print("*",end=" ")
#     print(sep=" ")
# for row in range(5,0,-1):
#     for space in range(5-row):
#         print(" ",end="")
#     for stars in range(row):
#         print("*",end=" ")
#     print()

'''    
    * 
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
#print 5 lined pyrmid with character beginning from 'A' take user input
num=int(input("Enter the no of rows: "))
n=int(input("Enter from which character you want to begin from: "))
for row in range(1,num+1):
    for space in range((num-row)):
        print(" ",end="")
    for char in range(row):
        print(chr(n),end=" ")
        n+=1
    print()
'''
    A 
   B C
  D E F
 G H I J
K L M N O
'''