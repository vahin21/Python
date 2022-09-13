# Program 1 - Factorial of a Number

# Variables
num = int(input("Enter a number: "))
f = 1

# Calculate the Factorial
for i in range(1, num+1):
    f = f*i

# Output the Factorial
print("The factorial of the number is ", f)