#wapt to get the below output..
#display 
# [1,2]
# [3,4]
# [5,6]
# [7,8]
# [9]
num=[1,2,3,4,5,6,7,8,9]
for i in range(0,len(num),2):#diplaying numbes go for 'range'
    print(num[i:i+2])
