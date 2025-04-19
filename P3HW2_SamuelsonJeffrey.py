#Jeffrey Samuelson
#4/19/2025
#P3HW2
#Working Overtime

# Request employee information
name = input('Enter employee name: ')
hours_worked = float(input('Enter number of hours worked this week: '))
pay_rate = float(input('Enter employee pay rate: '))

# Evaluate if overtime is worked with pay
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

# Display
print('------------------------------------------')
print(f'Employee Name: {name}')
print('------------------------------------------')
print(f"{'Hours Worked':<15}{'Pay Rate':<15}{'OverTime':<15}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<15}")
print('------------------------------------------------------------------------------------')
print(f"{hours_worked:<15}{pay_rate:<15}{ot_hours:<15.1f}{ot_pay:<15.2f}{reg_pay:<15.2f}{gross_pay:<15.2f}")
