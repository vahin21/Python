# Program 16 - Frequency of Digits in Dictionary

# Program to read a sentence and then create a dictionary that contains the frequency of digits.

# Variables
sen = input("Enter a sentence: ")
sen = sen.lower()
alpha_digits = "abcdefghijklmnopqrstuvwxyz1234567890"
char_count = {}

# Print Characters
print("Total Characters: ", len(sen))

# Find Frequencies
for char in sen:
    if char in alpha_digits:
        if char in char_count:
            char_count[char] = char_count[char] + 1
        else:
            char_count[char] = 1

# Print Char Count
print(char_count)