
from Class import Queue

def addJob( l, id, job ):
  l[id//100].enqueue([id, job])
  print('Job summitted')

def showList( l ):
  print('ID\tJobName')
  for i in range(10):
    size = len(l[i])
    for j in range(size):
      tmp = l[i].dequeue()
      print(tmp[0], '\t', tmp[1])
      l[i].enqueue(tmp)

def getNextJob( l ):
  for i in range(10):
    size = len(l[i])
    for j in range(size):
      tmp = l[i].dequeue()
      print('ID:', tmp[0], '\t', 'Job:', tmp[1], 'starts running')
      return

def cancelJob( l, id, job ):
  for i in range(10):
    size = len(l[i])
    for j in range(size):
      tmp = l[i].dequeue()
      if str(tmp[0]) == str(id) and str(tmp[1]) == str(job):
        print('ID:', tmp[0], '\t', 'Job:', tmp[1], 'has been cancelled')
        return
      l[i].enqueue(tmp)

def urgentJob( l, id, job ):
  l[0].enqueue([id, job])
  print('ID:', id, '\t', 'Job:', job, 'has first priority')

### ! Main ###
l = []
for i in range(10):
  l.append(Queue())
# l = [Queue0, Queue1, Queue2, ... , Queue9]
# Queue0 is for Urgent!
# Queue1 is for id 100-199 and so on

while True:
  inpt = list(input().split())
  # inpt = [code, id, job]
  if inpt[0] == 'A': addJob(l, int(inpt[1]), inpt[2])
  elif inpt[0] == 'L': showList(l)
  elif inpt[0] == 'R': getNextJob(l)
  elif inpt[0] == 'C': cancelJob(l, inpt[1], inpt[2])
  elif inpt[0] == 'U': urgentJob(l, inpt[1], inpt[2])
  elif inpt[0] == 'x': break
