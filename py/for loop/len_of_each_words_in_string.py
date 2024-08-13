#get length of each words from the string
s="This is a bunch of code"
words=s.split()
dictionary={}

for word in words:
    dictionary[word]=len(word)
print(dictionary)
