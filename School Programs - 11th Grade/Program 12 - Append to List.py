# Program 12 - Append to List

# Program to append an item to a list or extend a second list.

# Variables
x = [1, 2, 3, 4, 5, 6, 7]
print("List is ", x)

n = eval(input("Enter another list: "))

# Append or Extend to List
if type(x) == type(n):
    x.extend(n)
elif type(x) == type(1):
    x.append(n)
else:
    print("Invalid Data Type")

# Print Updated List
print("Updated List: ", x)