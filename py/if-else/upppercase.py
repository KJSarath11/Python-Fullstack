################ with using built in ######################
string=input("Enter the string: ")
# if string[0].isupper() :
#     print("Uppercase")
# else:
#     print("lowercase")

############ Without built in function of string ############

#string_check=ord(string[0]) #65 to 90 #using ord()
# if string_check>=65 and string_check<=90 :

if 'A'<=string[0]<='Z':
    print("upper")
else:
    print("lower")
#print(ord('Z'))