# Program 7 - Sum of Series

# Variables
n = int(input("Enter number of terms: "))
x = int(input("Enter value of x: "))
s = 1

# Calculate & Output
for a in range(1, n+1):
    s = s + x**a

print("Sum of Series: ", s)