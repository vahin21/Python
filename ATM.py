# Print the welcome message.
print("Welcome to ATM")

# Variables
restart=('Y')
chances = 3
balance = 100

# The conditions which the user chooses.
while chances >= 0:
    pin = int(input('Please Enter Your Pin: '))
    if pin == (8241):
        print('You entered the PIN Correctly.\n')
        while restart not in ('NO','no'):
            print('Enter 1 for Balance')
            print('Enter 2 for Withdrawl')
            print('Enter 3 for Adding Money in your Account')
            option = int(input('Your Choice: '))
            if option == 1:
                print('Your Balance is $',balance,'\n')
                restart = input('Would you like to go back: ')
                if restart in ('NO','no','n','N','No'):
                    print('Thank You')
                    break
                
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('Money to withdraw: '))     
                balance = balance - withdrawl
                print ('\nYour Balance is now $',balance)
                restart = input('Would You like to go back: ')
                if restart in ('NO','no','n','N','No'):
                        print('Thank You')
                        break  

            elif option == 3:
                Pay_in = float(input('How much would you add to your account: '))
                balance = balance + Pay_in
                print ('\nYour Balance is now $',balance)
                restart = input('Would You you like to go back: ')
                if restart in ('NO','no','n','N','No'):
                    print('Thank You')
                    break
    else:
        print("Wrong Pin Entered!")