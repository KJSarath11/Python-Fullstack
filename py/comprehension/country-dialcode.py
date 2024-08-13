#wapt dial codes
dial_code=[
    (86,'China'),
    (91,'India'),
    (92,'Pakistan'),
    (81,'Japan')
]
dict_={}

for item in dial_code:
    dict_[item[1]]=item[0]
print(dict_)

#comprehension
dict_={item[-1]:item[0] for item in dial_code}
print(dict_)