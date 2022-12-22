# Rock Paper Scissor - Game

# Imports
import random
import time

# Variables
result = ""
computerChoice = ""

# Play
def play(choice):
   choice = choice.lower()
   
   computer = random.randrange(1,4)

   if computer == 1: # Computer's Choice - Paper
      computerChoice = "Paper"

      if (choice == "paper"):
         result = "Draw"
      elif (choice == "rock"):
         result = "You Lose"
      elif (choice== "scissor"):
         result = "You Win"
   
   elif computer==2: # Computer's Choice - Rock
      computerChoice = "Rock"
   
      if (choice=="rock"):
         result = "Draw"
      elif (choice=="paper"):
         result = "You Win"
      elif (choice == "scissor"):
         result = "You Lose"
   
   elif computer==3: # Computer's Choice - Scissor
      computerChoice = "Scissor"
   
      if (choice=="rock"):
         result = "You Win"
      elif (choice=="scissor"):
         result = "Draw"
      elif (choice == "paper"):
         result = "You Lose"

   return {"result": result, "computer": computerChoice}
