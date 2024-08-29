# LUCKY NUMBER
from random import randint
def lucky_no(attempts=1):
    number = randint(1,20)
    #base
    if number == 13 :
        print(f"It took {attempts} attempts to generate 13")
        return None
    #recursive
    attempts+=1
    lucky_no(attempts)
    return(" ")
print(lucky_no())

