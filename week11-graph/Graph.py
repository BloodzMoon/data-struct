
def DFS( graph, v, vs=None ):
  # create variable only the first time
  visited = [False] * len(graph[0]) if vs is None else vs
  # set vertex to VISITED and print it
  visited[v] = True
  print(v, end=' ')
  # find every next vertex
  for i in range(len(graph[0])):
    if visited[i] is False and graph[v][i] != 0:
      DFS(graph, i, visited)

def BFS( graph, v ):
  # create variable only the first time
  visited = [False] * len(graph[0])
  queue = []
  # set first vertex to VISITED and enqueue
  visited[v] = True
  queue.append(v)
  # loop enqueue & pop then print
  while queue != []:
    tmp = queue.pop(0)
    print(tmp, end=' ')
    for i in range(len(graph[tmp])):
      if visited[i] is False and graph[tmp][i] != 0:
        visited[i] = True
        queue.append(i)
  
def findDist( graph, start, d=None, val=0 ):
  # ! DONT KNOW WHAT TO DO


def printGraph( graph ):
  # just print graph
  N = len(graph)
  for i in range(N):
    print('vertex', i, 'connected ', end='')
    for j in range(N):
      if graph[i][j] != 0:
        print(j, end=' ')
    print()
    