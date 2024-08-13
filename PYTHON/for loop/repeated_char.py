#wapt print only the repeated characters and count of the same.
s="helloworld"
count={}

for each_character in s:
    s.count(each_character)>1
    count[each_character]=s.count(each_character)#dictionary look up
print(count)