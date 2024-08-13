s="apple is a fruit"
vowels=set()#empty set

for char in s:
    if char in "aeiouAEIOU":
        vowels.add(char)
print(vowels)

#comprehension
{char for char in s if char in "aeiouAEIOU"}
print(vowels)