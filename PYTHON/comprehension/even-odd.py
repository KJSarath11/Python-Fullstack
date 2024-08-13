#wap to get square of even nos and cube of odd nos from a given list of integers

numbers=[2,3,4,5,6,7,8]
# even_odd=[]
# for item in numbers:
#     if item%2==0:
#         even_odd.append(item**2)
#     else:
#         even_odd.append(item**3)

# print(even_odd)

#comprehension
even_odd_=[(item**2) if item%2==0 else (item**3) for item in numbers]
print(even_odd_)