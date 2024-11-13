def find_max(li:list)->list:
    max=li[0]
    for num in li:
        if num>max:
            max=num
    return max

print(find_max([1, 3, 7, 2, 5]))  # Output: 7
print(find_max([-5, -2, -9, -1])) # Output: -1
