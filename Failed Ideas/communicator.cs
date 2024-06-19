using System;
using System.IO;
using Chess_Input;

class Communicator : Program
{
    static Random rd = new Random(); // initialize rng
    public static void Main()
    {
        // function to handle and verify integer inputs
        static int ReadInt(int min = int.MinValue, int max = int.MaxValue, int userInt = 0)
        {
            while (true)
            {
                bool isValid = int.TryParse(Console.ReadLine(), out userInt);

                if (isValid == false) // if input is not an integer
                {
                    Console.WriteLine("Please input a valid integer.");
                }
                else if (userInt < min || userInt > max) // if input is too little or too large
                {
                    Console.WriteLine("Out of range, please input a valid number.");
                }
                else { break; } // if input is valid
            }

            return userInt;
        }

        static string colourSelect()
        {

            Console.WriteLine("Enter the value for the piece colour you want to play as:\n1 = White\n2 = Black\n3 = Random");
            int colour = ReadInt(1, 3);
            switch (colour)
            {
                case 1:
                    return "White";

                case 2:
                    return "Black";

                case 3:
                    int draw = rd.Next(1, 2);
                    if (draw == 1)
                    {
                        return "White";
                    }
                    else
                    {
                        return "Black";
                    }
                default:
                    return "ERROR: Invalid Input";
            }

        }

        static int eloSelect()
        {
            int elo;
            while (true)
            {
                Console.WriteLine("Enter your current Chess ELO (0 to 3000): ");
                string tempELO = Console.ReadLine();
                bool result = int.TryParse(tempELO, out elo);
    
                if (result == false || tempELO.Contains('-') || elo <= 0 || elo > 3000)
                {
                    Console.WriteLine("Please enter a valid integer from 0 to 3000.");
                }
                else
                {
                    return elo;
                }
            }
        }

        // gets user's elo and uses it to calculate bot elo
        static int difficultySelect()
        {
            Console.WriteLine("Enter your desired difficulty\n1 = Easy\n2 = Medium\n3 = Hard\n4 = NIGHTMARE...");
            int difficulty = ReadInt(1, 4);
    
            switch (difficulty)
            {
                case 1:
                    return eloSelect() / 2;
    
                case 2:
                    return eloSelect();
    
                case 3:
                    return eloSelect() * 2;
    
                case 4:
                    return 3700;
    
                default:
                    return 0;
            }
        }

        // store values in variables
        string colour = colourSelect();
        string botELO = difficultySelect().ToString();
        string playerMove = moveInput();

        // write to file
        File.WriteAllText("communication.txt", colour);
        File.AppendAllText("communication.txt", $" {botELO}");
        File.AppendAllText("communication.txt", $" {playerMove}");
        }
    }