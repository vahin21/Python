# Program 8 - Fibonacci Series

# Variables
n = int(input("Enter number of terms: "))
f = 0
s = 1

# Print Variables
print(f)
print(s)

# Calculate Fibonacci Series
for i in range(2, n):
    t = f + s
    print(t)
    f = s
    s = t