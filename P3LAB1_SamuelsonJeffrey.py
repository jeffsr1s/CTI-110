#Jeffrey Samuelson
#4/19/2025
#P3LAB
#Here's your change

#Get input from user
change = float(input('Enter an amount of money. Please include the decimal: $'))

#Round for whole number division
change = round(change * 100)

#Determine how many dollars are needed
num_dollars = change // 100
change = change - (num_dollars * 100)

#Determine how many quarters are needed
num_quarters = change // 25
change = change - (num_quarters * 25)

#Determine how many dimes are needed
num_dimes = change // 10
change = change - (num_dimes * 10)

#Determine how many nickels are needed
num_nickels = change // 5
change = change - (num_nickels * 5)

#Number of pennies will be the leftover change amount
num_pennies = change

#Evaluate and display
if num_dollars > 0:
    if num_dollars == 1:
        print(f'{num_dollars} Dollar')
    else:
        print(f'{num_dollars} Dollars')

if num_quarters > 0:
    if num_quarters == 1:
        print(f'{num_quarters} Quarter')
    else:
        print(f'{num_quarters} Quarters')

if num_dimes > 0:
    if num_dimes == 1:
        print(f'{num_dimes} Dime')
    else:
        print(f'{num_dimes} Dimes')

if num_nickels > 0:
    if num_nickels == 1:
        print(f'{num_nickels} Nickel')
    else:
        print(f'{num_nickels} Nickels')

if num_pennies > 0:
    if num_pennies == 1:
        print(f'{num_pennies} Penny')
    else:
        print(f'{num_pennies} Pennies')

else:
    print(f"If you didn't need change why did you run a change program?")
