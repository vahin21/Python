# Program 10 - Pincode (Finds a Pincode in an Address)

# Variables
address = input("Enter an address: ")
addressList = address.split()

# Check for Pincode
for i in addressList:
    if (i.isdigit() and len(i) == 6):
        print("Pincode is ", i)
