using System;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Threading;
using System.Threading;
using System.Threading.Tasks;
using System.Xml.Serialization;
using ChessLogic;

namespace ChessUI
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        int prevMoveNum = -12121212;
        int moveNum;

        private readonly Image[,] pieceImages = new Image[8, 8];

        private GameState gameState;

        DispatcherTimer dispatcherTimer = new DispatcherTimer();


        public MainWindow()
        {
            

            InitializeComponent();
            InitializeBoard();

            gameState = new GameState(Player.White, Board.Initial());
            DrawBoard(gameState.Board);

            dispatcherTimer.Tick += DispatcherTimer_Tick;
            dispatcherTimer.Interval = TimeSpan.FromSeconds(1);
            dispatcherTimer.Start();
        }

        private void DispatcherTimer_Tick(object sender, EventArgs e)
        {
            moveNum = 1213;
            if (moveNum != prevMoveNum)
            {
                HandleMove();
            }
        }

        private void InitializeBoard()
        {
            for (int r = 0; r < 8; r++)
            {
                for (int c = 0; c < 8; c++)
                {
                    Image image = new Image();
                    pieceImages[r, c] = image;
                    PieceGrid.Children.Add(image);
                }
            }
        }

        private void DrawBoard(Board board)
        {
            for(int r = 0;r < 8; r++)
            {
                for (int c = 0; c < 8; c++)
                {
                    Piece piece = board[r, c];
                    pieceImages[r, c].Source = Images.GetImage(piece);
                }
            }
        }

        private void HandleMove()
        {

            gameState.MakeMove();
            DrawBoard(gameState.Board);
            prevMoveNum = moveNum;
        }

    }
}