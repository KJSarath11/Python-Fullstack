num1=[1,2,3,0,0,0]
num2=[2,5,6]
m=3
n=3
num1=num1[:m]
num2=num2[:n]
num1=num1+num2
num1.sort()
# num1[m:]=num2
print(num1)

s="hello developer"
print("Ommitting Start:",s[:5])#prints until 0-4
print("Ommitting end:",s[5:])#prints from 5