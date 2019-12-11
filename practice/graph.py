
graph = [ [0, 2, 0, 1, 0, 0, 0],          
          [0, 0, 0, 3, 10, 0,0],
          [4, 0, 0, 0, 0, 5, 0],
          [0, 0, 2, 0, 2, 8, 4],
          [0, 0, 0, 0, 0, 0, 6],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0] ]

# graph = [ [0, 2, 0, 1],          
#           [0, 0, 0, 3],
#           [4, 0, 0, 0],
#           [0, 0, 2, 0] ]


visited = [False] * len(graph)
# print(visited)


def DFS( graph, v, visited ):
  visited[v] = True
  print(v, end=' ')
  for i in range(len(graph[v])):
    if visited[i] == False and graph[v][i] != 0:
        DFS(graph, i, visited)


# x = [ [0, 1, 1, 0],
#       [0, 0, 1, 0],
#       [1, 0, 0, 1],
#       [0, 0, 0, 1] ]

def BFS( graph, v, visited, q=[] ):
  visited[v] = True
  q.append(v)
  while q != []:
    a = q.pop(0)
    print(a, end=' ')
    for i in range(len(graph[a])):
      if visited[i] is False and graph[a][i] != 0:
        q.append(i)
        visited[i] = True
        


# DFS(graph, 2, visited)
BFS(graph, 2, visited)

# for i in graph:
#   print(i)