'''from tkinter import *
  
root = Tk()
a = Label(root, text ="Hello World")
a.pack()

root.mainloop()'''

import random as r

def user_accept():
     flag = True
     while flag:
          enter1 = int(input("Enter row: ")) - 1
          enter2 = int(input("Enter column: ")) - 1
          if arr[enter1][enter2] == "O" or arr[enter1][enter2] == "X":
               print("Error")
               continue
          arr[enter1][enter2] = "X"
          break

def arr_print():
     for i in range(3):
          for j in range(3):
               print(arr[i][j], end=" ")
          print()

def comp_choice():
     flag = True
     while flag:
          comp1 = r.randrange(0,3)
          comp2 = r.randrange(0,3)

          if (arr[comp1][comp2] == "O" or arr[comp1][comp2] == "X"):
               continue

          arr[comp1][comp2] = "O"
          break

arr = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
user_accept()

comp_choice()
arr_print()
print(arr)
