import java.io.*;
import java.util.*;

/**
 * Conway's Game of Life by Team AreWeSentientYet?
 * Jihae Park
 * collaborators: Seth Adams, Shana Elizabeth Henry, Marisa Shuman
 */

/**
   The Rules of Life:

   Survivals:
   * A living cell with 2 or 3 living neighbours will survive for the next generation.

   Deaths:
   * Each cell with >3 neighbours will die from overpopulation.
   * Every cell with <2 neighbours will die from isolation.

   Births:
   * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

   NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.
*/

public class Cgol
{

  //create, initialize, and return  empty board (all cells dead) 
  public static char[][] createNewBoard( int rows, int cols ) //1
  {
    char[][] board = new char[rows][cols];                                                       
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        board[i][j]='-';
      }
    }
    return board;
  }


  //print the board to the terminal 
  public static void printBoard( char[][] board ) //3
  {
    for (int i = 0; i < board.length; i++) 
    {
      for (int j = 0; j < board[i].length; j++) //i instead of row??
      {
        System.out.print(board[i][j] + " "); 
      }
      System.out.println("");
    }
  }


  //set cell (r,c) to val 

  //make the new random population
  // int deadOrAliveTest = random.nextint(10) +1
  public static void setCell( char[][] board, int r, int c, char val ) //2
  {
    board [r][c] = val;
  }


  //return number of living neigbours of board[r][c] 
  public static int countNeighbours( char[][] board, int r, int c ) //4
  {
    int count = 0;
    int rows = board.length;
    int cols = board[0].length;
    
    //iterate through the nine neighboring cells 
    for (int i = r-1; i <= r+1; i++) {
      for (int j = c-1; j <= c+1; j++) {
        //if the current cell is the targeted cell, then skip the code below and continue with the incremented value in the above for loop
        if (i == r && j == c){
          continue;
        }
        //i >= 0 is to check if the left top corner is not out of the bound
        if ((i >= 0 && i < rows) && (j >= 0 && j < cols)) {
            if (board[i][j] == 'X') {
              count ++;
            } 
        }   
      }
    }
    return count;
  }

    //start at the r to the top left -- iterate over that until it is at the bottom right. count -- think of it as creating a square of 8 around the specific indicated cell and is iterating over all of those cells.
 

  /**
     precond: given a board and a cell
     postcond: return next generation cell state based on CGOL rules
     (alive 'X', dead '-')
  */
  
  //check the conditions for live/dead
  //a live cell with fewer than 2 live neighbors dies, as if by underpopulation
  //a live cell with more than 3 live neighbors dies, as if by overpopulation
  //a dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction
  public static char getNextGenCell( char[][] board,int r, int c ) //5
  {
    //initialize the number of live neighbors 
    int numAlive = countNeighbours(board, r, c);
    //a live cell with fewer than 2  or more than 3 live neighbors dies
    if (board[r][c] == 'X' && (numAlive < 2 || numAlive > 3)){
      return '-';
    } //a dead cell with exactly 3 live neighbors becomes a live cell 
    else if (board[r][c] == '-' && numAlive == 3){
      return 'X';    
    }
    return board[r][c];
  }


  //generate and return a new board representing next generation
  public static char[][] generateNextBoard( char[][] board ) //6
  {
    //create a new variable to hold a new temporary board
    //iterate through the entire original board and run the getNextGenCell() on it and store the result in the new temporary board
    //return the new temporary board
    char[][] tempBoard = createNewBoard(board.length, board[0].length);   
    for(int i = 0; i < board.length; i++){
      for(int j = 0; j < board[0].length; j++){
        tempBoard[i][j] = getNextGenCell(board, i, j);
      }
    }
    return tempBoard;
  }


  public static void main( String[] args )
  {
    
    char[][] board;
    board = createNewBoard(10,10);
    int gen = 1;
    //breathe life into some cells:
    setCell(board, 1, 1, 'X');
    setCell(board, 2, 1, 'X');
    setCell(board, 3, 1, 'X');
    
    System.out.println("Gen " + gen + ":");
    printBoard(board);
    System.out.println("--------------------------\n\n");
    
    System.out.println(countNeighbours(board,0,0));
    
    board = generateNextBoard(board);
    
    gen ++;
    System.out.println("Gen " + gen + ":");
    printBoard(board);
    System.out.println("--------------------------\n\n");
    
    board = generateNextBoard(board);

    gen ++;
    System.out.println("Gen " + gen + ":");
    printBoard(board);
    System.out.println("--------------------------\n\n");
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    // TASK:
    // Once your initial version is running,
    // try out different starting configurations of living cells...
    // (Feel free to comment out the above three lines.)

    System.out.println("Gen X:");
    printBoard(board);
    System.out.println("--------------------------\n\n");

    board = generateNextBoard(board);

    System.out.println("Gen X+1:");
    printBoard(board);
    System.out.println("--------------------------\n\n");
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
  }//end main()

}//end class