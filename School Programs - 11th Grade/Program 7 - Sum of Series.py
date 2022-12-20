# Program 7 - Sum of Series

# Program to calculate the sum of the series 1 + x2 + x3 + x4...

# Variables
n = int(input("Enter number of terms: "))
x = int(input("Enter value of x: "))
s = 1

# Calculate & Output
for a in range(1, n+1):
    s = s + x**a

print("Sum of Series: ", s)
