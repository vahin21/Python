# Program 13 - Frequencies of Elements

# Program to find frequencies of elements of a list. Also, print the list of unique elements in the list and duplicate elements in the given list.

# Variables
n = eval(input("Enter the list: "))
length = len(n)
uniq = []
dupl = []

count = i = 0

# Check Frequencies
while i<length:
    element = n[i]
    count = 1

    if (element not in uniq) and (element not in dupl):
        i += 1

        for j in range(i, length):
            if (element == n[j]):
                count += 1
        else:
            print("Element ", element, "Frquency ", count)

            if count == 1:
                uniq.append(element)
            else:
                dupl.append(element)
    else:
        i += 1

# Print the Lists
print(n)
print(uniq)
print(dupl)