#1.wapt to print the string along with its length using map...
# names=["apple","googel"]
# def func(args):
#     return (args,len(args))#accepting multiple inputs 
# res=map(func,names)
# print(next(res))

#2.wapt to print the square and cube of a number using map...
# nums=[1,2,3,4,5]
# res=map(lambda num:(num**2,num**3),nums)
# print(next(res))


#3.wapt to find if a given list of strings starts with 'a'
# names=["Alex","stebe","anna","henry"]
# res=map(lambda args:args if args[0] in "aA" else None,names)
# for i in res:
#     print((i))

#4.wapt to convert -ve to +ve
# nums=[1,-8,-3,4,-7]
# res=map(lambda num:abs(num),nums)
# for i in res:
#     print(i)

#5.wapt to return a list of elements raused to the power of their indices..
# nums=[1,2,3,4]
# indices=list(range(0,len(nums)))
# res=map(lambda n1,n2:n1**n2,nums,indices)
# for i in res:
#     print(i)

#6.wapt to claculate the sum of only positive numbers of a given list...
# nums=[1,-8,-3,4,-7]
# res=sum(list(map(lambda num:num if num>0 else 0,nums)))
# print(res)

#7.square the even nos only
# r=range(0,21)
# res=list(map(lambda num:num**2 if num%2==0 else None,r))
# #making a list makes it easy to print,else we have to go for using the 'next' multiple times..
# print((res))