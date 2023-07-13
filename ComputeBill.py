#Rate per day
rpd = 15000
#Sound system fee
ssf = 4500
#Stage decor fee
sdf = 3000
#Catering fee
cf = 350000

#Expanded Value Added Tax
EVAT = .12

#Input where the program ask the user to enter the number of day/s.
numdays = int(input("Enter The Number of Day/s: "))


#The processes to solve the bill
Amount = rpd * numdays

TotalAmount = Amount + ssf + sdf + cf

Tax = TotalAmount * EVAT

Bill = TotalAmount + Tax

#Display the bill.
print(Bill)


