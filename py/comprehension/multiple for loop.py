#multiple for loops in comprehension
#o/p=[1,2,3,4,5,6,7,8,9]
matrix=[1,2,3],[4,5,6],[7,8,9]
# flattened=[]

# for each_item in matrix:
#     for each_number in each_item:
#         flattened.append(each_number)
# print(flattened)


flattened_=[number for item in matrix for number in item]
print(flattened_)