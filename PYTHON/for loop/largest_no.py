#wapt find the largest number in the list without using any inbuilt functions..
numbers=[10,20,30,40,50]
largest_no=numbers[0]

for each_no in numbers:
    if largest_no<each_no:
        largest_no=each_no 
print(largest_no)
    

