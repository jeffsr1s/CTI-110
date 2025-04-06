#Jeffrey Samuelson
#4/5/2025
#P1HW2
#Plan a trip

print("This program calculates and displays travel expenses")
#Get info from user
budget = int(input("Enter budget: "))
dest = input("Enter your travel destination: ")
gas_exp = int(input("How much do you think you will spend on gas? "))
accom = int(input("How much do you estimate you will need for accomodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

#Add expenses
total_exp = gas_exp + accom + food
#Subtract expenses from budget
balance = budget - total_exp

#Whitespace
print()

#Display results
print("------------Travel Expenses------------")
print("Location:", dest)
print("Initial budget:", budget)

#Whitespace
print()

print("Fuel:", gas_exp)
print("Accomodation:", accom)
print("Food:", food)
print()
print("Remaining balance:", balance)