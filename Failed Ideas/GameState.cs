using System;
using System.Collections.Generic;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ChessLogic
{
    public class GameState
    {
        public Board Board { get; }
        public Player CurrentPlayer { get; private set; }

        public GameState(Player player, Board board)
        {
            CurrentPlayer = player;
            Board = board;
        }


        public void MakeMove() 
        {
            Move move;

            move.FromPos.Row = 1;
            move.FromPos.Column = 0;
            move.ToPos.Row = 2;
            move.ToPos.Column = 0;

             move.Execute(Board);
            CurrentPlayer = CurrentPlayer.Opponent();
        }
    }
}
