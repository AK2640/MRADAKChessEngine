# import libraries
import random
import gui

# initialize rng
random.seed()

# function to read and validate an integer input
def read_int(min_value=999999999, max_value=999999999, user_int=0):
  while True: # loop to continuously prompt user for an acceptable value
    try:
      user_int = int(input())
      if user_int < min_value or user_int > max_value:
        print("Out of range, please input a valid number.")
      else:
        break
    except ValueError:
      print("Please input a valid integer.")
  return user_int

# function to prompt user for piece color to play
def colour_select():
  print("Enter the value for the piece colour you want to play as:\n1 = White\n2 = Black\n3 = Random")
  colour = read_int(1, 3)
  if colour == 1:
    return "White"
  elif colour == 2:
    return "Black"
  elif colour == 3:
    return random.choice(["White", "Black"])
  else:
    return "ERROR: Invalid Input"


# function to prompt user for their elo
def elo_select():
  while True:
    try:
      temp_elo = input("Enter your current Chess ELO (0 to 3000): ")
      elo = int(temp_elo)
      if elo < 0 or elo > 3000:
        print("Please enter a valid integer from 0 to 3000.")
      else:
        return elo
    except ValueError: # if an incorrent value type is given, print following message
      print("Please enter a valid integer from 0 to 3000.")


# function to prompt user for a difficulty, then return the bot elo accordingly
def difficulty_select():
  print("Enter your desired difficulty\n1 = Easy\n2 = Medium\n3 = Hard\n4 = NIGHTMARE...")
  difficulty = read_int(1, 4)
  if difficulty == 1: # easy
    return elo_select() // 2
  elif difficulty == 2: # medium
    return elo_select()
  elif difficulty == 3: # hard
    return elo_select() * 2
  elif difficulty == 4: # nightmare
    return 3700
  else:
    pass

# store values into variables
colour = colour_select()
bot_elo = str(difficulty_select())
player_move = moveInput()  # using move input from gui program

# write values to txt file
with open("communication.txt", "w") as file:
  file.write(colour)
  file.write(f" {bot_elo}")
  file.write(f" {player_move}")
