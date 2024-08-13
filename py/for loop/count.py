#program to count the number of digits and alphabets in the string
string="hai 1234 pytho23"
alphabet_count=0
digit_count=0

for each_character in string:
    if each_character.isalpha():
        alphabet_count+=1
    elif each_character.isdigit():
        digit_count+=1

print(f"Alphabets:{alphabet_count} Digits:{digit_count}")