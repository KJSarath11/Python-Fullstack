string = input("Enter the string: ")
result = ""
special_character = False

for char in string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char
    elif not (65 <= ord(char) <= 90 or 97 <= ord(char) <= 122):
        special_character = True
        break

if special_character:
    print("Special characters are found")
else:
    print(result)
