s="hello world"
string=""
for char in s:
    if s.count(char)>1:
        string=string+"*"
    else:
        string+=char
print(string)