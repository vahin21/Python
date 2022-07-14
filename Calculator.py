# Calculator Program

# Functions - Operations
def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def modulus(x, y):
   return x % y
def exponenciation(x, y):
   return x ** y
def floorDivision(x, y):
   return x // y

# Print & Input
print("What do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Exponenciation")
print("7. Floor Division")
choice = input("Enter Choice (1/2/3/4/5/6/7): ")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

# What operation the user wants to do.
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
elif choice == '5':
   print(num1, "%",num2,"=", modulus(num1, num2))
elif choice == '6':
   print(num1, "**",num2,"=", exponenciation(num1, num2))
elif choice == '7':
   print(num1, "//",num2,"=", floorDivision(num1, num2))
else:
   print("Invalid input")
