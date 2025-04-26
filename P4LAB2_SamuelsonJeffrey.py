#Jeffrey Samuelson
#4/26/2025
#P4LAB2
#Multiplication tables with while loop and for loop

#Run program
run_again = "yes"

#Run until we get no
while run_again != "no":

    #Get an integer from the user
    user_num = int(input("Enter an integer: "))

    #If number is positive display multiplication table for 1-12
    if user_num >= 0:
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")

    #If number is negative tell user program cannot accept
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

#Loop has broken. User entered 'no'
print("Program is ending...")
