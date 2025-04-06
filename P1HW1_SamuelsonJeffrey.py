#Jeffrey Samuelson
#4/5/2025
#P1HW1
#Expressing integers

print("-----Calculating Exponents----")
#Get input from user
base_value = int(input("Enter an integer as the base value: "))
exp = int(input("Enter an integer as the exponent: "))

#Perform expression
result = base_value ** exp

#Whitespace line
print()

#Show result to user
print(f"{base_value} raised to the power of {exp} is {result}!!")

#Whitespace line
print()

print("-----Addition and Subtraction----")

#Whitespace line
print()

#Get input from user
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

#Whitespace line
print()

#Perform expression
add_sub = num1 + num2 - num3

#Whitespace line
print()

#Reveal result to user
print(f"{num1} + {num2} - {num3} is equal to {add_sub}")