# Program 17 - Create Third Dictionary

# Program to create a third dictionary from two dictionaries having common keys.

# Variables
dict1 = {"1": 100, "2": 200, "3": 300}
dict2 = {"1": 300, "2": 200, "5": 400}

# Check Common Keys
for i, j in dict1.items():
    for x, y in dict2.items():
        if (i == x):
            dict3[i] == (j+y)

# Print New Dictionary
print(dict3)