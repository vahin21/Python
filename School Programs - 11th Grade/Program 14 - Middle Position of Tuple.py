# Program 14 - Middle Position of Tupe

# Program to check if the minimum element of a tuple lies at the middle position of the tuple.

# Variables
tup = eval(input("Enter the tuple: "))
ln = len(tup)
lies = False
mn = min(tup)

# Check if it lies in the middle.
if (ln % 2 == 0):
    half = ln//2

    if (mn == tup[half] or mn == tup[half-1]):
        lies = True
else:
    half = ln//2

    if mn == half[half]:
        lies = True

# Print if it lies in the middle.
if lies == True:
    print("Minimum lies in the middle.")
else:
    print("No")