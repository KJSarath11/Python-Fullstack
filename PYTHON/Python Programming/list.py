numbers_list = [3, 4, 5, 6]  # List of numbers
dict_ = {}

# Traverse the list and populate the dictionary based on the condition
for key, value in enumerate(numbers_list):
    # If index is even, the value must also be even
    if key % 2 == 0 and value % 2 == 0:
        dict_[key] = value
    # If index is odd, the value must also be odd
    elif key % 2 != 0 and value % 2 != 0:
        dict_[key] = value

# Print the dictionary
print(dict_)
