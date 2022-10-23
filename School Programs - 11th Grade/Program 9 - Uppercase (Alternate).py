# Program 9 - Uppercase (Alternate) It capitalizes each alternate letter in a word.

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
