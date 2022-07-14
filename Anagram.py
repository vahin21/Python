# Anagram Program

# Functions
def lengthOfStrings(a, b):
    if (len(a) == len(b)):
        return True
    else:
        return False

def sortStrings(a, b):
    if (sorted(a) == sorted(b)):
        return True
    else:
        return False

# Take 2 Strings
string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

# Check if its an Anagram
if (lengthOfStrings(string1, string2) == True and sortStrings(string1, string2) == True):
    print("It is an anagram!")
else:
    print("They are not anagrams.")
