#Jeffrey Samuelson
#4/26/2025
#P4HW1
#Grades with loops

score_num = int(input("How many scores would you like to enter? "))
print()

#empty list
scores = []

for num in range(1, score_num + 1):
    #collect scores
    score = float(input("Enter your score #" + str(num) + ":"))
    #evaluate entry
    while score < 0 or score > 100:
        print("INVALID SCORE ENTERED!!!")
        print("Score should be between 0 and 100")
        score = float(input("Enter your score #" + str(num) + " again: "))
    scores.append(score)
    print()

#copy scores to a list we can change
scores_modified = scores

#find lowest score and drop it
lowest = min(scores)
scores_modified.remove(lowest)

#calculate average with our changed scores
avg = sum(scores_modified)/len(scores_modified)

#determine letter grade for average
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

#display results
print("--------------Results----------------")
print(f"Lowest score: {lowest}") 
print(f"Modified list: {scores_modified}")
print(f"Scores average: {avg:.2f}")
print(f"Grade: {grade}")
print("-------------------------------------")
