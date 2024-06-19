# Program: Chess Engine
# Section Written By: Aarav Kohli
# Date: 6/5/2024
# Unit: ICS3U Culminating
# Description: A program that implements and optimizes
# The stockfish algorithm to work for the purposes of the project.



from stockfish import Stockfish
import chess

stockfish = Stockfish(path=r"./stockfish-windows-x86-64-avx2.exe") # Intialize Stockfish
playerIsWhite = False # Set the player to Black by Default
currentMoves = [] # Create an array for moves

# Define a function to split the contents of the array into an array

def readFile():
    return open("communication.txt", "r").read().split(" ")
    
# Define a function to write contents to the file, not overriding it

def writeToFile(content):
    f = open("communication.txt", "a")
    f.write(" " + content)
    f.close()

# Define a file to override the contents of the file

def overrideFile(content):
     f = open("communication.txt", "w")
     f.write(content)
     f.close()
   
# Check if the player is playing as white or black, and set the boolean

if readFile()[0] == "White":
   playerIsWhite = True

elo = readFile()[1] # Set the Elo
depth = 15 # Set the search depth
   

class engineSetup:

    # Set the game difficulty

    def setGameDifficulty(self, elo, depth):
     stockfish.set_elo_rating(elo)
     stockfish.set_depth(depth)


    # Allow the player to ake a move

    def makePlayerMove(self, move):
         if stockfish.is_move_correct(move):
          currentMoves.append(move) 

    # Return the position as a FEN

    def getFen(self):
        return stockfish.get_fen_position()
    
class chessGame(engineSetup):
    pass # Inherit methods from engine setup
    e = engineSetup()
    chess.Board(e.getFen()) # Set the chessboard

    def playMovesWhite(e):
        currentMoves.append(stockfish.get_best_move()) # Add Stockfish's move
        print(currentMoves)
        print(readFile())
        stockfish.set_position(currentMoves) # Change the stockfish position
        writeToFile(currentMoves[len(currentMoves) - 1]) # Write Stockfishes move to the file
        print(readFile())
        move = readFile()[len(readFile()) -1]
        e.makePlayerMove(move)
        print(currentMoves)
        stockfish.set_position(currentMoves) # Update Stockfish Position
        chess.Board(e.getFen()) # Update the chessboard

    def playMovesBlack(e):
        currentMoves.append(readFile()[len(readFile()) - 1]) # Append the user's first move
        print(currentMoves)
        print(readFile())
        stockfish.set_position(currentMoves) # Update the stockfish position
        currentMoves.append(stockfish.get_best_move()) # Update the moves with stockfish's move
        print(currentMoves)
        print(readFile())
        stockfish.set_position(currentMoves) # Set the stockfish position
        writeToFile(currentMoves[len(currentMoves) - 1]) # Write the move to the file
        move = readFile()[len(readFile()) -1] # Find the player's move
        e.makePlayerMove(move) # Make the move
        print(currentMoves)
        print(readFile())
        stockfish.set_position(currentMoves) # Update Stockfish's position
        chess.Board(e.getFen()) # Update the Chessboard

    e.setGameDifficulty(elo, depth)

    while(playerIsWhite and not chess.Board(e.getFen()).is_checkmate()):
        if len(readFile()) % 2 == 0:  
          playMovesWhite(e)
   
    while(not playerIsWhite and not chess.Board(e.getFen()).is_checkmate()):
        if len(readFile()) % 2 != 0:  
          playMovesBlack(e)


overrideFile("#")


  
