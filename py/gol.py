# gol
# Jihae Park
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 


#create, initialize, and return  empty board (all cells '-') 
def createNewBoard(numRows, numCols):
  board = []
                
  for i in range(numRows): 
    row = []
    for j in range(numCols): 
      row.append('-')

    board.append(row)

  return board


#print the board to the terminal 
def printBoard(board):

  for rows in range(len(board)):
    for cols in range(len(board[rows])):
      print(board[rows][cols], end = " ")  
    print()
  

#set cell (r,c) to val 

#make the new random population
#  '-'Or'X'Test = random.next(10) +1
def setCell(board, r, c, val):

  board[r][c] = val


#return number of living neigbours of board[r][c] 
def countNeighbours(board, r,  c):

  count = 0
  rows = len(board)
  cols = len(board[0])
  
  #iterate through the nine neighboring cells 
  for i in range(r - 1, r + 2, 1):
    for j in range(c - 1, c + 2, 1): 
      #if the current cell is the targeted cell, then skip the code below and continue with the incremented value in the above for loop
      if (i == r and j == c):
        continue
      
      #i >= 0 is to check if the left top corner is not out of the bound
      if ((i >= 0 and i < rows) and (j >= 0 and j < cols)):
          if (board[i][j] == 'X'):
            count += 1

  return count


  #start at the r to the top left -- iterate over that until it is at the bottom right. count -- think of it as creating a square of 8 around the specific indicated cell and is iterating over all of those cells.


#
#   printecond: given a board and a cell
#   postcond: return next generation cell state based on #CGOL rules
#  ('X' 'X', '-' '-')
#

#check the conditions for live/'-'
#a live cell with fewer than 2 live neighbors dies, as if by underpopulation
#a live cell with more than 3 live neighbors dies, as if by overpopulation
#a '-' cell with exactly 3 live neighbors becomes a live cell, as if by reprintoduction
def getNextGenCell(board, r,  c ):

  #initialize the number of live neighbors 
  numAlive = countNeighbours(board, r, c)
  #a live cell with fewer than 2  or more than 3 live neighbors dies
  if (board[r][c] == 'X' and (numAlive < 2 or numAlive > 3)):
    return '-'
   #a '-' cell with exactly 3 live neighbors becomes a live cell 
  elif (board[r][c] == '-' and numAlive == 3):
    return 'X'    
  
  return board[r][c]



#generate and return a new board reprintesenting next generation
def generateNextBoard(board):

  #create a new variable to hold a new temporary board
  #iterate through the entire original board and run the getNextGenCell() on it and store the result in the new temporary board
  #return the new temporary board
  tempBoard = createNewBoard(len(board), len(board[0]))   
  for i in range(len(board)):
    for j in range(len(board[0])):
      tempBoard[i][j] = getNextGenCell(board, i, j)
    
  return tempBoard


#main function 
def main():

  board = createNewBoard(10,10)
  gen = 1
  #breathe life o some cells:
  setCell(board, 1, 1, 'X')
  setCell(board, 2, 1, 'X')
  setCell(board, 3, 1, 'X')
  
  print("Gen", gen, ":")
  printBoard(board)
  print("--------------------------\n\n")
  
  print(countNeighbours(board,0,0))
  
  board = generateNextBoard(board)
  
  gen += 1
  print("Gen", gen, ":")
  printBoard(board)
  print("--------------------------\n\n")
  
  board = generateNextBoard(board)

  gen += 1
  print("Gen", gen, ":")
  printBoard(board)
  print("--------------------------\n\n")

  # TASK:
  # Once your initial version is running,
  # try out different starting configurations of living cells...
  # (Feel free to comment out the above three lines.)

#call main funciton
main()

# DONE!!