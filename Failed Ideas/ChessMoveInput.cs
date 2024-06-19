using System.Diagnostics;

namespace Chess_Input
{
    public class Program
    {

        public static string moveInput()
        {
            int move;
            string rawInput = "";
            bool error;
            int fromPosLetter, toPosLetter;
            do
            {
                error = false;
                Console.WriteLine("Enter Move as location of piece you want to move and then the location you want to move it to.\nEx.\tyou want to move a piece from A1 to B3 you would type that as \"A1B3\"\n\n\n");
                rawInput = ReadString("Please enter your move:\t");
                fromPosLetter = PosProcessing(rawInput, 0);
                toPosLetter = PosProcessing(rawInput, 2);
                if (rawInput == "")
                {
                    Console.WriteLine("\nPlease enter a value.");
                    error = true;
                } else if (int.TryParse(rawInput.Substring(1, 1), out int trash) == false || int.TryParse(rawInput.Substring(3, 1), out int trash1) == false || int.Parse(rawInput.Substring(1, 1)) > 8 || int.Parse(rawInput.Substring(1, 1)) < 1 || int.Parse(rawInput.Substring(3, 1)) > 8 || int.Parse(rawInput.Substring(3, 1)) < 1 || fromPosLetter == 10 || toPosLetter == 10 || rawInput.Length != 4)
                {
                    Console.WriteLine("Ensure move is entered correctly\n\n");
                    error = true;
                }
            } while (error == true);

            int fromPosNum = int.Parse(rawInput.Substring(1, 1));
            int toPosNum = int.Parse(rawInput.Substring(3, 1));
            int fromPos = (fromPosLetter * 10) + fromPosNum;
            int toPos = (toPosLetter * 10) + toPosNum;
            move = (fromPos * 100) + toPos;

            return rawInput.ToString();
        }

        public static string ReadString(string prompt)
        {
            Console.Write(prompt);
            return Console.ReadLine();
        }

        static int PosProcessing(string raw, int picker) 
        {
                string Letter = raw.Substring(picker, 1);
                Letter = Letter.ToUpper();
                switch (Letter) 
                {
                    case "A":
                        return 1;
                    case "B":
                        return 2;
                    case "C":
                        return 3;
                    case "D": 
                        return 4;
                    case "E":
                        return 5;
                    case "F":
                        return 6;
                    case "G":
                        return 7;
                    case "H":
                        return 8;
                    default:
                        return 10;
                }
        }
    }
}
