# Written By: Aarav Kohli with Mitchel Reigert, and Aaron Dam
# Course: ICS3U
# Date: 6/19/2024
# Program Description: This program takes in the input parameters
# From the JSON File, and Plays Chest Against the User in a 
# GUI


# Imports
from tkinter import *
import json
from stockfish import Stockfish

stockfish = Stockfish(path=r"./stockfish-windows-x86-64-avx2.exe") # Intialize Stockfish
currentMoves = [] # Array For Moves
stringToGiveUser = stockfish.get_board_visual() # Set Base Chess Board
Font_tuple = ("Courier New", 20, "bold") # Font settings


def playMovesWhite():
    currentMoves.append(moveEntry.get()) # Append the User's move to the list
    stockfish.set_position(currentMoves) # Update Stockfish Position
    currentMoves.append(stockfish.get_best_move()) # Add Stockfish's move
    stockfish.set_position(currentMoves) # Update Stockfish Position
    stringToGiveUser = stockfish.get_board_visual() # Set the Board visual (string)
    computerText.configure(text=stringToGiveUser, font=Font_tuple) # Change the text on the GUI

def playMovesBlack():
    currentMoves.append(moveEntry.get()) # Append the User's move to the list
    stringToGiveUser = stockfish.get_board_visual() # Set the Board visual (string)
    computerText.configure(text=stringToGiveUser, font=Font_tuple) # Change the text on the GUI
    stockfish.set_position(currentMoves) # Update Stockfish Position
    currentMoves.append(stockfish.get_best_move()) # Add Stockfish's move
    stockfish.set_position(currentMoves) # Update the stockfish position
    stringToGiveUser = stockfish.get_board_visual()  # Set the Board visual (string)
    computerText.configure(text=stringToGiveUser, font=Font_tuple) # Change the text on the GUI

colour = 1 # Define colour

# Opening JSON file
with open('settings.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
    colour = json_object["Colour"]
    stockfish.set_elo_rating(json_object["Elo"])

# Define Tkinter Root
root = Tk()
root.title('MRADAK Engine')

# Make the Title
w = Label(root, text='MRADAK Engine')
w.pack(anchor='w', padx=20, pady=10) 


# If the User is playing as black
if colour == 1:
    instructions = Label(root, text="Enter a Move") # Tell them to enter a move
    moveEntry = Entry(root) # Make the input box
    stockfish.set_position(currentMoves) # Change the stockfish position
    currentMoves.append(stockfish.get_best_move()) # Add Stockfish's move
    stockfish.set_position(currentMoves) # Update Stockfish Position
    stringToGiveUser = stockfish.get_board_visual() # Update board string
    submit = Button(root, text="Submit", height=1, width=5, command=playMovesWhite) # Submit Button
    computerText = Label(root, text=stringToGiveUser, font=Font_tuple) # Board Visual

    # Pack Widgets
    instructions.pack(anchor='w', padx=20, pady=10)
    moveEntry.pack(anchor='w', padx=20, pady=10)
    submit.pack(anchor='w', padx=20, pady=10)
    computerText.pack()
    root.mainloop()

# If the User is playing as white
if colour == 2:
    instructions = Label(root, text="Enter a Move")  # Tell them to enter a move
    moveEntry = Entry(root) # Make the input box
    submit = Button(root, text="Submit", height=1, width=5, command=playMovesBlack) # Submit Button
    computerText = Label(root, text=stringToGiveUser, font=Font_tuple) # Board Visual

    # Pack Widgets
    instructions.pack(anchor='w', padx=20, pady=10)
    moveEntry.pack(anchor='w', padx=20, pady=10)
    submit.pack(anchor='w', padx=20, pady=10)
    computerText.pack()
    root.mainloop()
