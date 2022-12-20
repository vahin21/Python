# Program 5 - Upper Case

# Program to print whether a given character is uppercase/lowercase/digit or any other character.

# Variables
ch = intput("Enter character: ")

# Check if it is Upper Case
if (ch >= 'A' and ch <= 'Z'):
    print("Upper Case")
elif (ch >= 'a' and ch <= 'z'):
    print("Lower Case")
elif (ch >= '0' and ch <= '9'):
    print("It's a number.")
else:
    print("It is a special character.")
