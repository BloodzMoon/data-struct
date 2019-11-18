
def createBoard( size ):
  board = []
  for i in range(size):
    tmp = []
    for j in range(size):
      tmp.append('.')
    board.append(tmp)
  return board


def printBoard( board ):
  for row in board:
    for column in row:
      print(column, end=' ')
    print()
  print()


def isSafe( board, row, column ):
  # check row
  if not isRowSafe(board, row, column):
    return False
  # check column
  if not isColumnSafe(board, row, column):
    return False
  # check diagonal
  if not isDiagonalSafe(board, row, column):
    return False
  # THIS PLACE IS SAFE!!
  return True


def isRowSafe( board, row, column ):
  r, c = row, column
  while r > -1:
    if board[r][c] is 'Q':
      return False
    r -= 1
  return True


def isColumnSafe( board, row, column ):
  r, c = row, column
  while c > -1:
    if board[r][c] is 'Q':
      return False
    c -= 1
  return True


def isDiagonalSafe( board, row, column ):
  r, c = row, column
  while r > -1 and c > -1: # left upper diagonal
    if board[r][c] is 'Q':
      return False
    r, c = r-1, c-1
  r, c = row, column
  while r > -1 and c < len(board[0]): # right upper diagonal
    if board[r][c] is 'Q':
      return False
    r, c = r-1, c+1
  return True


def placeQueen( board, n, row=0, column=0 ):
  # try to place Queen
  if isSafe(board, row, column):
    board[row][column] = 'Q'
    n -= 1
    # if completed show solution!!
    if n is 0:
      printBoard(board)
    # else place Queen in other row
    else:
      if row+1 < len(board):
        placeQueen(board, n, row+1, 0)
    # pop Queen out of board to try other solution
    board[row][column] = '.'
    n += 1
  # try other solution
  if column+1 < len(board[0]):
    placeQueen(board, n, row, column+1)
  


# ! MAIN
b = createBoard(4)
placeQueen(b, 4)
    