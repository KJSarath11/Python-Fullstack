#counting number of each char in a string
my_string="guido van rossumn"
count={}
for char in my_string:
    count[char]=my_string.count(char)
print(count)

#comprehension
count={char:my_string.count(char)for char in my_string}
print(count)
