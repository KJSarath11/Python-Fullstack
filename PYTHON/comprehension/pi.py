#####_genereate all pi values_######(nb)
from math import pi
res=[]
for i in range(0,6):
    res.append(round(pi,i))
print(res)

# comprehension
res=[round(pi,i)for i in range(0,6)]
print(res)