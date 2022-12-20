# Program 2 - Number Pattern

# Program to print a number patern.

# Variables
r = int(input("Enter number of rows: "))
y = 2

# Output the Rows
for i in range(1, r+1):
    for j in range(1, i):
        print(y, end=" ")
        y += 2
    
    print()
