#Jeffrey Samuelson
#4/11/2025
#P2HW1
#Clean up display for the plan a trip P1HW2

print("This program calculates and displays travel expenses")

# Get info from user
budget = float(input("Enter budget: "))
dest = input("Enter your travel destination: ")
gas_exp = float(input("How much do you think you will spend on gas? "))
accom = float(input("How much do you estimate you will need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Add expenses
total_exp = gas_exp + accom + food
# Subtract expenses from budget
balance = budget - total_exp

# Whitespace
print()

# Display results
print("------------Travel Expenses------------")
print("Location:".ljust(20), dest)
print("Initial budget:".ljust(20), f"${budget:.2f}")
print()
print("Fuel:".ljust(20), f"${gas_exp:.2f}")
print("Accommodation:".ljust(20), f"${accom:.2f}")
print("Food:".ljust(20), f"${food:.2f}")
print("---------------------------------------")
print()
print("Remaining Balance:".ljust(20), f"${balance:.2f}")
