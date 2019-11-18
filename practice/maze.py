
# * can only walk RIGHT and DOWN  
def findWay( maze, x=0, y=0 ):
  if x < len(maze) and y < len(maze[0]):
    if maze[x][y] == 'P':
      showWay(maze)
      return
    elif maze[x][y] == 'X':
      return
    elif maze[x][y] == ' ':
      maze[x][y] = '.'
      # * move right
      findWay(maze, x, y+1)
      # * move down
      findWay(maze, x+1, y)
      # * back tracking
      maze[x][y] = ' '
    
def showWay( maze ):
  for row in maze:
    for column in row:
      print(column, end=' ')
    print()
  print()

def makeMaze( liststring ):
  maze = []
  for row in liststring:
    tmp = []
    for column in row:
      tmp.append(column)
    maze.append(tmp)
  return maze


# ! MAIN
maze = [
   '   X ', 
   ' X X ', 
   '     ', 
   ' X X ', 
   'X   P']
m = makeMaze(maze)
findWay(m)