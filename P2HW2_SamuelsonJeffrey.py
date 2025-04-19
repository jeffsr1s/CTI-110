#Jeffrey Samuelson
#4/11/2025
#P2HW2
#Student grades

#Get test grades for each module from user
grade1 = float(input('Enter grade for Module 1: '))
grade2 = float(input('Enter grade for Module 2: '))
grade3 = float(input('Enter grade for Module 3: '))
grade4 = float(input('Enter grade for Module 4: '))
grade5 = float(input('Enter grade for Module 5: '))
grade6 = float(input('Enter grade for Module 6: '))

#Create a list using the input
grades_list = [grade1,grade2,grade3,grade4,grade5,grade6]

#Calculate using functions of a list
min_grade = min(grades_list)
max_grade = max(grades_list)
sum_grade = sum(grades_list)
avg_grade = sum(grades_list)/len(grades_list)

#Display
print()
print('------------Results------------')
print('Lowest Grade:'.ljust(20), f'{min_grade}')
print('Highest Grade:'.ljust(20), f'{max_grade}')
print('Sum of Grades:'.ljust(20), f'{sum_grade}')
print('Average:'.ljust(20), f'{avg_grade:.2f}')
print('-------------------------------')
