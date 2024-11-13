# n=int(input("Enter the no: "))
# k=1
# for row in range(1,n+1):
#     for num in range(1,row+1):
#         if row%2==1:
#             print(k,end=" ")
#         else:
#             print("*", end=" ")
#     if row%2==0:
#         k+=1
#     print()
'''
1
* *
2 2 2
* * * *
3 3 3 3 3 '''

# n=int(input("Enter the no: "))
# k=1
# for row in range(1,n+1):
#     for space in range((n)-row):
#         print(" ",end=" ")
#     for num in range(1,row+1):
#         if row%2==1:
#             print(k,end=" ")
#         else:
#             print("*", end=" ")
#     if row%2==0:
#         k+=1
#     print()
''' 
        1
      * *
    2 2 2
  * * * *
3 3 3 3 3
'''

# for row in range(1,6):
#     for num in range(1,6):
#         if row==num:
#             print("$",end=" ")
#         elif row+num==6:
#             print("$",end=" ")
#         else:
#             print(num,end=" ")
        
#     print()
'''
$ 2 3 4 $ 
1 $ 3 $ 5
1 2 $ 4 5
1 $ 3 $ 5
$ 2 3 4 $'''

for row in range(1,6):
    for num in range(1,6):
        if row==num:
            print(num,end=" ")
        elif row+num==6:
            print(num,end=" ")
        else:
            print("$",end=" ")
    print()
'''
1 $ $ $ 5 
$ 2 $ 4 $
$ $ 3 $ $
$ 2 $ 4 $
1 $ $ $ 5   '''