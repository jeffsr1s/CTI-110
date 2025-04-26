#Jeffrey Samuelson
#4/26/2025
#P4HW2
#Multiple employees getting paid

# Create variables for totals
total_ot_pay = 0
total_reg_pay = 0
total_gross_pay = 0
employee_count = 0

# Create empty list
employees = []

# Request employee information inside loop
while True:
    name = input("Enter employee's name or \"Done\" to terminate: ")
    if name == "Done":
        break  # Exit without storing "Done"

    hours_worked = float(input(f"Enter number of hours {name} worked this week: "))
    pay_rate = float(input(f"What is {name}'s pay rate: "))

    # Calculate pay details
    if hours_worked > 40:
        ot_hours = hours_worked - 40
        ot_pay = ot_hours * (pay_rate * 1.5)
        reg_pay = 40 * pay_rate
        gross_pay = reg_pay + ot_pay
    else:
        ot_hours = 0
        ot_pay = 0
        reg_pay = hours_worked * pay_rate
        gross_pay = reg_pay

    # Update total variables
    total_ot_pay += ot_pay
    total_reg_pay += reg_pay
    total_gross_pay += gross_pay
    employee_count += 1 

    # Store employee data to the list
    employees.append((name, hours_worked, pay_rate, ot_hours, ot_pay, reg_pay, gross_pay))

# Display all individual employee information after termination
print("\nEMPLOYEE PAYROLL REPORT")
print('------------------------------------------')
for employee in employees:
    name, hours_worked, pay_rate, ot_hours, ot_pay, reg_pay, gross_pay = employee
    print(f'Employee Name: {name}')
    print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
    print('------------------------------------------------------------------------------------')
    print(f"{hours_worked:<15}{pay_rate:<15}{ot_hours:<15.1f}{ot_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}")
    print("\n")  # Add spacing between employees for clarity

# Final summary after termination
print("\nFINAL PAYROLL SUMMARY")
print('------------------------------------------')
print(f"Total Employees Processed: {employee_count}")
print(f"Total Overtime Pay: ${total_ot_pay:.2f}")
print(f"Total Regular Pay: ${total_reg_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")
print('------------------------------------------')

print("Program terminated. All employee payroll calculations complete.")
