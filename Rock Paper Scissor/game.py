# Game - Rock Paper Scissor

# Imports
import random
import time

# Variables
final = ""
computerChoice = ""

# Play Function
def play(choice):
   computer = random.randrange(1,4)

   # Computer Choice - Paper, Rock, Scissor
   if computer==1: # Computer's Choice - Paper
      computerChoice = "Paper"

      if (choice == "paper"):
         final = "Draw"
      elif (choice == "rock"):
         final = "You Lose"
      elif (choice== "scissor"):
         final = "You Win"
   
   elif computer==2: # Computer's Choice - Rock
      computerChoice = "Rock"
   
      if (choice=="rock"):
         final = "Draw"
      elif (choice=="paper"):
         final = "You Win"
      elif (choice == "scissor"):
         final = "You Lose"
   
   elif computer==3: # Computer's Choice - Scissor
      computerChoice = "Scissor"
   
      if (choice=="rock"):
         final = "You Win"
      elif (choice=="scissor"):
         final = "Draw"
      elif (choice == "paper"):
         final = "You Lose"

   return {"Final": final, "Computer": computerChoice}
