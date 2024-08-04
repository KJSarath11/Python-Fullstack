engineering=["ME","CS","EE","EC"]
per=int(input("Enter the percentage: "))
name=input("Enter the name: ")

if per>75:
    if per>85:
        print(f"Dear {name} you are eligible to taken\n"
              f"{'\n'.join(engineering)}")
        option=input("Enter the option :")
        if option in engineering:
            print("You have choosen {option} option.")
        else:
            print("You have cant choose {option} option.")
    else: 
        print(f"Dear {name} you are eligible to taken\n"
              f"{'\n'.join(engineering[2::])}")
        option=input("Enter the option :")
        if option in engineering[2::]:
            print("You have choosen {option} option.")
        else:
            print("You have cant choose {option} option.")
else:
    print("You are not eligible to join any courses.")

