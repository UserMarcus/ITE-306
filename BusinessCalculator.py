print("BUSINESS CALCULATOR MENU")
print("1] Simple Interest")
print("2] Compound Interest")
print("3] Exit")

choice = input("Choose [1/2/3]: ")

if choice == '1':
    principal= int(input("Enter the Principal Amount: "))
    interest_rate = int(input("Enter Interest Rate: "))
    time = int(input("Enter Time (in years)"))
    interest = principal * interest_rate * time
    print("Simple Interest: ", interest)

elif choice == '2':
    principal = int(input("Enter the Principal Amount: "))
    rate = float(input("Enter Rate: "))
    time = int(input("Enter Time (in years)"))
    compound_interest = principal * pow((1 + (rate/100)),time)
    print("Compound Interest: ", compound_interest)

elif choice == '3':
    print("Thank you for using my Business Calculator.")

else:
    print("Invalid choice. Please select a valid option.")



\
