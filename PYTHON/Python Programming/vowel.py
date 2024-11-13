def count_vowels(s:str)->int:
    vowels="aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count 

print(count_vowels("hello"))        # Output: 2
print(count_vowels("programming"))  # Output: 3
