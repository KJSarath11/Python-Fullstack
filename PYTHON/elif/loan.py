loan_amount=int(input("Enter the loan amount: "))
print("Choose for:-\n1.Personal Loan\n2.Car Loan\n3.House Loan\n")
option=int(input("Enter the option: "))

if option==1:
    interest=loan_amount*.11
    print(f"Loan Amount:{loan_amount}")
    print(f"Total Amount:{loan_amount+interest}")

elif option==2:
    interest=loan_amount*.09
    print(f"Loan Amount:{loan_amount}")
    print(f"Total Amount:{loan_amount+interest}")

elif option==3:
    interest=loan_amount*.07
    print(f"Loan Amount:{loan_amount}")
    print(f"Total Amount:{loan_amount+interest}")
    
else:
    print("Invalid input.")
