# Program 9 - Uppercase (Alternate)

# Program to turn each alternate letter of a string uppercase.

# Variables
word = input("Enter a word: ")
wordList = []
s = 1

# Check for Uppercase
for i in word:
    if (s%2==0):
        b = i.upper()
        wordList.append(b)
    else:
        wordList.append(i)

    s += 1

# Create the Word
finalWord = "".join(wordList)
print(finalWord)
