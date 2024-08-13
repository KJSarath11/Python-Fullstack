Karnataka={"Bangalore","Hasan","Mysore"}
Kerla={"Thrissur","Ernakulam","Kollam"}
Tamilnadu={"Chennai","Ooty"}

country=input("Enter the country: ")#country

if(country=='India'):
    state=input("Enter the city: ")#state
    if(state in Karnataka):
        print(f"Welcome to {state} in Karnataka.")
        
    elif(state in Kerla):
        print(f"Welcome to {state} in Kerala.")
    elif(state in Tamilnadu):
        print(f"Welcome to {state} in Tamilnadu.")
else:
    print("No India No Life")