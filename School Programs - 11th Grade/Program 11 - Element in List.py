# Program 11 - Element in List

# Program to find a given element in a list.

# Variables
x = eval(input("Enter the list: "))
n = int(input("Enter a number: "))
length = len(x)

# Find Element
for i in range(0, length):
    if (n == x[i]):
        print(n, ' is located at index ', i)
        break
else:
    print("Nope")