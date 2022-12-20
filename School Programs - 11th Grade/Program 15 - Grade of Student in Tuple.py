# Program 15 - Grade of Student in Tuple

# Program to calculate the grade of the student in a tuple.

# Variables
mks = eval(input("Enter marks tuple: "))
total = sum(mks)
avg = total/5

# Check Grade
if (avg >= 75):
    grade = "A"
elif (avg >= 60):
    grade = "B"
elif (avg >= 50):
    grade = "c"
else:
    grade = "D"

# Print the Grade
print("The grade is ", grade)