#flipping keys and values in dictionary using dict comprehension
d={'a':1,'b':2,'c':3}
flipped={}
for key,value in d.items():
    flipped[value]=key
print(flipped)

#comprehension
flipped={value:key for key,value in d.items()}
print(flipped)