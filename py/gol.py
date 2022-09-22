# gol
# Jihae Park
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 

#create, initialize, and return  empty board (all cells dead) 
def createNewBoard(rows, cols):

  board = new char[rows][cols]                                                       
  for i in rows: 
    for j in cols: 
      board[i][j]='-'
    
  
  return board



#print the board to the terminal 
def printBoard(board):

  for ( i = 0 i < board.length i++) 
  
    for ( j = 0 j < board[i].length j++) #i instead of row??
    
      System.out.print(board[i][j] + " ") 
    
    print("")
  



#set cell (r,c) to val 

#make the new random population
#  deadOrAliveTest = random.next(10) +1
def setCell(board, r, c, val):

  board [r][c] = val



#return number of living neigbours of board[r][c] 
def countNeighbours(board, r,  c):

   count = 0
   rows = board.length
   cols = board[0].length
  
  #iterate through the nine neighboring cells 
  for ( i = r-1 i <= r+1 i++) 
    for ( j = c-1 j <= c+1 j++) 
      #if the current cell is the targeted cell, then skip the code below and continue with the incremented value in the above for loop
      if (i == r and j == c):
        continue
      
      #i >= 0 is to check if the left top corner is not out of the bound
      if ((i >= 0 and i < rows) and (j >= 0 and j < cols)):
          if (board[i][j] == 'X'):
            count ++
           
         
    
  
  return count


  #start at the r to the top left -- iterate over that until it is at the bottom right. count -- think of it as creating a square of 8 around the specific indicated cell and is iterating over all of those cells.


#
#   printecond: given a board and a cell
#   postcond: return next generation cell state based on #CGOL rules
#  (alive 'X', dead '-')
#

#check the conditions for live/dead
#a live cell with fewer than 2 live neighbors dies, as if by underpopulation
#a live cell with more than 3 live neighbors dies, as if by overpopulation
#a dead cell with exactly 3 live neighbors becomes a live cell, as if by reprintoduction
def getNextGenCell(  board, r,  c ):

  #initialize the number of live neighbors 
   numAlive = countNeighbours(board, r, c)
  #a live cell with fewer than 2  or more than 3 live neighbors dies
  if (board[r][c] == 'X' and (numAlive < 2 or numAlive > 3)):
    return '-'
   #a dead cell with exactly 3 live neighbors becomes a live cell 
  elif (board[r][c] == '-' and numAlive == 3):
    return 'X'    
  
  return board[r][c]



#generate and return a new board reprintesenting next generation
def generateNextBoard(board):

  #create a new variable to hold a new temporary board
  #iterate through the entire original board and run the getNextGenCell() on it and store the result in the new temporary board
  #return the new temporary board
   tempBoard = createNewBoard(board.length, board[0].length)   
  for( i = 0 i < board.length i++)
    for( j = 0 j < board[0].length j++)
      tempBoard[i][j] = getNextGenCell(board, i, j)
    
  
  return tempBoard



def main():

  
   board
  board = createNewBoard(10,10)
   gen = 1
  #breathe life o some cells:
  setCell(board, 1, 1, 'X')
  setCell(board, 2, 1, 'X')
  setCell(board, 3, 1, 'X')
  
  print("Gen " + gen + ":")
  printBoard(board)
  print("--------------------------\n\n")
  
  print(countNeighbours(board,0,0))
  
  board = generateNextBoard(board)
  
  gen ++
  print("Gen " + gen + ":")
  printBoard(board)
  print("--------------------------\n\n")
  
  board = generateNextBoard(board)

  gen ++
  print("Gen " + gen + ":")
  printBoard(board)
  print("--------------------------\n\n")
/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  # TASK:
  # Once your initial version is running,
  # try out different starting configurations of living cells...
  # (Feel free to comment out the above three lines.)

  print("Gen X:")
  printBoard(board)
  print("--------------------------\n\n")

  board = generateNextBoard(board)

  print("Gen X+1:")
  printBoard(board)
  print("--------------------------\n\n")
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*/
#end main()

#end class