# MRADAKChessEngine
Source code for the MRADAK chess engine written for the ICS3U Culminating.

# Components

The Chess Engine has originally had three Files: The Engine, the Conversion, and the GUI.

Engine: The Engine uses Python , and was written by Aarav Kohli.

Conversion: The Conversion uses pure Python, and was written by Aaron Dam.

GUI: The GUI was Written using C# by Mitchell Riegert. 

The Chess Engine now has two files: The Setup GUI, and the Game. This is because some technical
errors persisted in C#, forcing us to migrate to Python. At this point, the project was close to
the due date which made it easier to make the entire project on one device. All members contributed 
equally, even when not writting code however.

It is also important to note that the original GUI was going to be a full chess board, however time
constraints forced it to be a string that the user can interact with.

# Important Note

To run the code in the program, please download the AVX2 Version of StockFish from https://stockfishchess.org/download/
Extract the ZIP Folder, and place the: stockfish-windows-x86-64-avx2.exe file in the same directory as the entire project.

Alternatively, the file directory in game.py can be changed to access the file on the windows operating system.

# Installation

To ensure all libraries are working properly, please run the following command in the cloned repository (Windows).

      pip install stockfish

  Note: Tkinter comes preinstalled in python. To check Python's version, run the following command:

       python --version

# Failed Versions Folder

As mentioned earlier, there were many failed revisions of this project. The code for each failed file is included
in a seperate folder to show our work.

# Tuning

Given the computational power that stockfish requires, tuning the engine may be neccessary to allow it to run optimally.

To change the amount of CPU Cores and quantity of RAM the engine uses, insert the following command in game.py:

      stockfish.update_engine_parameters({"Hash": 2048, "Threads": 3})

The Hash parameter updates the amount of RAM the engine uses, and must be a power of 2. The threads count can
be modified depending on your machine specifications, however you should not exceed the number of cores
your CPU has.
      

