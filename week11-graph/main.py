
from Graph import *

g = [ [0, 2, 0, 1,  0, 0, 0],          
      [0, 0, 0, 3, 10, 0, 0],
      [4, 0, 0, 0,  0, 5, 0],
      [0, 0, 2, 0,  2, 8, 4],
      [0, 0, 0, 0,  0, 0, 6],
      [0, 0, 0, 0,  0, 0, 0],
      [0, 0, 0, 0,  0, 1, 0] ]

print('\n\n\n\n\n\n\n\n\n\n')
printGraph(g)
print()

print('Breathe First Search : ', end='')
BFS(g, 2)
print()

print('Depth First Search : ', end='')
DFS(g, 2)
print()

# print(findDist(g,0))