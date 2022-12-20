# Program 10 - Pincode

# Program to find a pincode in an address (string).

# Variables
address = input("Enter an address: ")
addressList = address.split()

# Check for Pincode
for i in addressList:
    if (i.isdigit() and len(i) == 6):
        print("Pincode is ", i)
