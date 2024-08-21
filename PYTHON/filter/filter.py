#1.Passing 0-20 and returning square of only even nos
# r=range(0,21)
# even=list(filter(lambda num:num%2==0,r))
# res=list(map(lambda num:num**2,even))
# print(res)

#2.sum of only postitive
# nums=[1,-8,-3,4,-7]
# positive=sum(list(filter(lambda num:num>0,nums)))
# print(positive)

#3.only even length string using filter 
# names=["apple","google","yahoo","facebook"]
# res=list(filter(lambda name:len(name)%2==0,names))
# print(res)

#4.return thr string if string is starting in vowel
# names=["apple","google","yahoo","facebook","APPLE"]
# res=list(filter(lambda name:name[0] in "aeiouAEIOU",names))
# print(res)

#5.divisible by both 5 and 3
# nums=[15,30,35,56,78]
# res=list(filter(lambda num:num%3==0 and num%5==0,nums))
# print(res)

#6.prices greater than 100
# prices={'acme':45.63,'aapl':612.56}
# res=list(filter(lambda item:item[-1],prices))
# print(res)
