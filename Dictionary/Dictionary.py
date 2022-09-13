# Imports
import json
from difflib import get_close_matches

# Load the JSON file.
data = json.load(open("data.json", encoding="utf8"))

# Function - Meaning & Correction
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Function - Ask the User
def ask():
    word = input("Enter Word: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
            userChoice = input("Would You Like to Get Another Meaning (Y/N): ")
            if (userChoice == "N"):
                break
            else:
                ask()
    else:
        print(output)

ask()
