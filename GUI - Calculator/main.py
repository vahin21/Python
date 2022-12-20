# Main - GUI Calculator

# Imports
from tkinter import *

# Initialization
win = Tk()
win.eval('tk::PlaceWindow . center')

# Config
win.geometry("312x324")
win.resizable(0, 0)
win.title("GUI Calculator")

# Functions

# 1) Button Click
def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 2) Clear the Field
def text_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

# 3) Evaluate the String
def equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

expression = ""

# Input Text 
input_text = StringVar()

# Frame
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1.5)
input_frame.pack(side=TOP)

# Input Field
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame Button
btns_frame = Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()

# First Row
clear = Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: text_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

# Second Row
seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

# Third Row
four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# Fourth Row
one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# Fourth Row
zero = Button(btns_frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#dedede", cursor = "hand2", command = lambda: equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

# Run the GUI
win.mainloop()