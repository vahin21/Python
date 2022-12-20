# Program 6 - Average Marks

# Program to calculate average marks of a user.

# Variables
math = int(input("Enter math marks: "))
sci = int(input("Enter science marks: "))
eng = int(input("Enter English marks: "))

# Calculate Average
avg = (math + sci + eng) / 3
print(avg)

# Check Percentage
if (avg >= 80):
    print("Grade: A")
elif (avg >=70 and avg < 80):
    print("Grade: B ")
elif (avg >=60 and avg < 70):
    print("Grade: C")
elif (avg >= 50 and avg < 60):
    print("Grade: D")
else:
    print("Grade: E")
