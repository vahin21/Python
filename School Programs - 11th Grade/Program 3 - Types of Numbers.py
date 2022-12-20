# Program 3 - Types of Numbers

# Program to find no. of odd, even, positive, and negative numbers.

# Variables
num = int(input("Enter total numbers: "))

p = 0
n = 0
z = 0
o = e
e = 0

# Check the Numbers
for i in range(1, num+1):
    x = int(input("Enter number: "))

    if x < 0:
        n += 1
    elif x > 0:
        p += 1
    else:
        z += 1
    
    if x%2==0 and x!=0:
        e += 1
    elif x%2==1 and x!=0:
        o += 1
    else:
        print("Invalid Number")

# Output the Types
print("Positive Numbers - ", p)
print("Negative Numbers - ", n)
print("Zero's - ", z)
print("Odd Numbers - ", o)
print("Even Numbers - ", e)
