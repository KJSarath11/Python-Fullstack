database={7038:"steve",6300:"jack",7795:"michel"}
# reg_no=int(input("Enter the reg ni: "))
name=input("Enter your name: ")
#checks keys only...
if name in database[name]:
    subject=input("Enter the subject: ")
    if subject=="python":
        print(f"Mr/ms {database[name]} you are welcome {subject} class")
    elif subject=="sql":
        print(f"Mr/ms {database[name]} you are welcome {subject} class")
    else:
        print(f"Mr/ms {database[name]} you are not welcome to this class")
else:
    print("please contact your councelor")
    

    