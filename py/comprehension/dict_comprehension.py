################ DICTIONARY_COMPREHENSION ###############
#string
s="This is a bunch of code"
dict_={}
for item in s.split():
    dict_[item]=len(item)
print(dict_)

#comprehension
dict_={item:len(item) for item in s.split()}
print(dict_)
