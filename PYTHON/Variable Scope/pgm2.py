# print thr numbers from 'n' to 0 without using 'while'
from time import sleep
# def countdown(n):
#     #base case
#     if n>-1:
#         print(f"counting down {n}")
#         sleep(1)
#         #recursive case
#         countdown(n-1)
#     return(" ") 
# print(countdown(5))

# print thr numbers from '0' to n without using 'while' or 'for'

#   WHILE
# def countup(start,stop):
#     while(start<=stop):
#         print("")

# def countup(start,stop):
#     if start<=stop:
#         print(f"Counting up..{start}")
#         sleep(1)
#         countup(start+1,stop)
#     return(" ")
# print(countup(0,5))

#alternative way for thr above
def count(stop):
    def run(start):
        if start<=stop:
            print(f"Counting up...{start}")
            sleep(0.5)
            start+=1
            run(start)
    return(run(start=0))

print(count(5))


