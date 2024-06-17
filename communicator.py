import random

def read_int(min_value=int.min, max_value=int.max, user_int=0):
  """
  This function reads integer input from the user with validation.
  """
  while True:
    try:
      user_int = int(input())
      if user_int < min_value or user_int > max_value:
        print("Out of range, please input a valid number.")
      else:
        break
    except ValueError:
      print("Please input a valid integer.")
  return user_int

def colour_select():
  """
  This function prompts the user for piece color and returns it.
  """
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

def elo_select():
  """
  This function prompts the user for ELO and returns it after validation.
  """
  while True:
    try:
      temp_elo = input("Enter your current Chess ELO (0 to 3000): ")
      elo = int(temp_elo)
      if elo < 0 or elo > 3000:
        print("Please enter a valid integer from 0 to 3000.")
      else:
        return elo
    except ValueError:
      print("Please enter a valid integer from 0 to 3000.")

def difficulty_select():
  """
  This function prompts the user for difficulty and returns calculated bot ELO.
  """
  print("Enter your desired difficulty\n1 = Easy\n2 = Medium\n3 = Hard\n4 = NIGHTMARE...")
  difficulty = read_int(1, 4)
  if difficulty == 1:
    return elo_select() // 2
  elif difficulty == 2:
    return elo_select()
  elif difficulty == 3:
    return elo_select() * 2
  elif difficulty == 4:
    return 3700
  else:
    pass

# Main program logic
colour = colour_select()
bot_elo = str(difficulty_select())
player_move = moveInput()  # Assuming moveInput() is defined elsewhere

# Write to file
with open("communication.txt", "w") as file:
  file.write(colour)
  file.write(f" {bot_elo}")
  file.write(f" {player_move}")