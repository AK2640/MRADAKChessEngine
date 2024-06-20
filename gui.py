# Written By: Aarav Kohli with Mitchell Riegert, and Aaron Dam
# Course: ICS3U
# Date: 6/19/2024
# Program Description: This program sets up 
# The Stockfish Engine, to Be Played in the Next GUI

# Imports
from tkinter import *
import json
import subprocess
import random

# Variables
elo = 1000
difficulty = 4
colour = 1

hasEnteredOptions = False # Exists for further revisions in which the entire game is one GUI (Can't change Parameters Midgame)
move = ""

# Tkinter Initialized

root = Tk()
root.title('MRADAK Engine')
root.resizable(False, False)

# Function to Set the Player to White
def setWhite():
    global hasEnteredOptions, colour  
    if not hasEnteredOptions:
        # Set the colour while the user is still able to
        colour = 2


# Function to Set the Player to Random
def setRand():
    global hasEnteredOptions, colour  
    if not hasEnteredOptions:
        # Set the colour while the user is still able to
        colour = random.randint(1, 2) # Random Colour


# Function to Set the Difficulty to Easy
def setEasy():
    global hasEnteredOptions, difficulty 
    if not hasEnteredOptions:
        difficulty = 1 # Set the difficulty while the user is still able to

# Function to Set the Difficulty to Medium
def setMedium():
    global hasEnteredOptions, difficulty 
    if not hasEnteredOptions:
        difficulty = 2 # Set the difficulty while the user is still able to

# Function to Set the Difficulty to Hard
def setHard():
    global hasEnteredOptions, difficulty 
    if not hasEnteredOptions:
        difficulty = 3 # Set the difficulty while the user is still able to

# Function to Set the Difficulty to Hardest
def setNightmare():
    global hasEnteredOptions, difficulty 
    if not hasEnteredOptions:
        difficulty = 4 # Set the difficulty while the user is still able to

# Function to get the User's Elo and set the global variable
def getElo():
    global elo
    elo = int(T.get())

# Function to Lock in the Settings and Close the GUI
def closeOptions():
    global hasEnteredOptions, difficulty
    getElo() # Set Elo
    hasEnteredOptions = True # Close Setting Selection
    computerElo = 0 # Create Computer Elo

    root.destroy() # Close the GUI

    # Change the Computer Elo based on teh difficulty
    if difficulty == 1:
        computerElo = elo / 2
    elif difficulty == 2:
        computerElo = elo
    elif difficulty == 3:
         computerElo = elo * 2
    elif difficulty == 4:
        computerElo = 4000

    # Create a dictionary for neccessary Data
    toFile = {
        "Colour": colour,
        "Elo": computerElo
    }

    # Serializing json
    json_object = json.dumps(toFile, indent=4)
 
    # Writing to json
    with open("settings.json", "w") as outfile:
        outfile.write(json_object)

    # Run the Game.py file with subprocess
    subprocess.run(["python", "game.py"])


    

# Title
w = Label(root, text='MRADAK Engine')
w.pack(anchor='w', padx=20, pady=10)

# Instructions
instructions = Label(root, text="Please enter the following information:\n\n")
instructions.pack(anchor='w', padx=20)

# Colour Heading
colourText = Label(root, text="What Colour Would you Like to Play As?")
colourText.pack(anchor='w', padx=20) 

# Black Button
blackButton = Checkbutton(root, text="Black")
blackButton.pack(anchor='w', padx=40)

# White Button
whiteButton = Checkbutton(root, text="White", command=setWhite)
whiteButton.pack(anchor='w', padx=40) 

# Random button
randButton = Checkbutton(root, text="Random", command=setRand)
randButton.pack(anchor='w', padx=40)

# Elo Text
eloText = Label(root, text="What is your Elo?")
eloText.pack(anchor='w', padx=20, pady=(10, 0))

# Text Entry for Elo
T = Entry(root)
T.pack(anchor='w', padx=40)

# Difficulty Text
difficultyText = Label(root, text="Select your Difficulty:")
difficultyText.pack(anchor='w', padx=20)

# Easy Button
easyButton = Checkbutton(root, text="Easy", command=setEasy)
easyButton.pack(anchor='w', padx=40)

# Medium Button
mediumButton = Checkbutton(root, text="Medium", command=setMedium)
mediumButton.pack(anchor='w', padx=40)

# Hard Button
hardButton = Checkbutton(root, text="Hard", command=setHard)
hardButton.pack(anchor='w', padx=40)

# Nightmare Button
nightmareButton = Checkbutton(root, text="Nightmare", command=setNightmare)
nightmareButton.pack(anchor='w', padx=40)

# Button to start
continueButton = Button(root, text="Start", height=1, width=5, command=closeOptions)
continueButton.pack(anchor='w', padx=20, pady=10) 


root.mainloop()
