# for i in range(1,6):
#     for j in range(1,6):
#         if i==1:
#             print(j,end=" ")
#         if i>1 and j==1:
#             print(sep=" ")
#             print(i,end="")
'''
1 2 3 4 5 
2
3
4
5
'''

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
''' 
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j,end=" ")
#     print(sep=" ")
'''
5 
5 4
5 4 3
5 4 3 2
5 4 3 2 1
'''

# for row in range(1,6):
#     for num in range(row):
#             print(row,end=" ")
#     print()
'''
1 
2 2
3 3 3
4 4 4 4
5 5 5 5 5   '''

# for row in range(5,0,-1):
#     for num in range(row):
#             print(row,end=" ")
#     print()
'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1   '''

# for row in range(5,0,-1):
#     for num in range(6-row):
#             print(row,end=" ")
#     print()
'''
5 
4 4
3 3 3
2 2 2 2
1 1 1 1 1'''