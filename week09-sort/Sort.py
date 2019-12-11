
def bubbleSort( l ):
  for last in reversed(range(len(l))):
    for i in range(last):
      if l.index(i).data > l.index(i+1).data:
        l.index(i).data, l.index(i+1).data = l.index(i+1).data, l.index(i).data

def selectionSort( l ):
  for last in reversed(range(len(l))):
    Max = last
    for i in range(last):
      if l.index(i).data > l.index(Max).data:
        Max = i
    l.index(Max).data, l.index(last).data = l.index(last).data, l.index(Max).data

def insertionSort( l ):
  for cur in range(1, len(l)):
    insert = l.index(cur).data
    for i in reversed(range(cur+1)):   
      if insert < l.index(i-1).data and i > 0:
        l.index(i).data = l.index(i-1).data
      else:
        l.index(i).data = insert
        break

def shellSort( l ):
  for shell in reversed(range(1, 6, 2)): # 5, 3, 1
    s = []
    for n in range(shell):
      s.append(LinkedList())
    for i in range(len(l)):
      print(isinstance(l.index(i).data, LinkedList.Node))
      # TODO: dsalkdfsekzsfljlawejslfkdlksweshdklsekldlxkfklezmsdlfmzesl;mds
      s[i%shell].append(l.index(i).data)
    for ele in s:
      insertionSort(ele)
    for i in range(len(l)):
      l.index(i).data = s[i%shell].removeHead()

def mergeSort( l, _left=None, _right=None ):
  left = 0 if _left is None else _left
  right = len(l)-1 if _right is None else _right
  center = (left + right)//2
  if left < right:
    mergeSort(l, left, center)
    mergeSort(l, center+1, right)
    merge(l, left, center+1, right)

def merge( l, A, B, B_end):
  a, a_end = A, B-1
  b, b_end = B, B_end
  result = []
  while a <= a_end and b <= b_end:
    if l.index(a).data < l.index(b).data:
      result.append(l.index(a).data)
      a += 1
    else:
      result.append(l.index(b).data)
      b += 1
  while a <= a_end:
    result.append(l.index(a).data)
    a += 1
  while b <= b_end:
    result.append(l.index(b).data)
    b += 1
  for ele in result:
    l.index(A).data = ele
    A += 1

def quickSort( l, low=None, high=None, count=None ): 
  low = 0 if low is None else low
  high = len(l)-1 if high is None else high
  count = 0 if count is None else count

  if low < high: 
    pi = partitionLast(l,low,high) 
    # pi = partitionMid(l,low,high) 
    # pi, count = partitionFirst(l,low,high) 

    count += quickSort(l, low, pi-1, count) 
    count += quickSort(l, pi+1, high, count) 
  return count

def partitionLast( l, low, high ): # pivot last
  i, j, pivot = low, high-1, high

  while True:
    while l.index(i).data < l.index(pivot).data:
      i += 1
    while l.index(j).data > l.index(pivot).data:
      j -= 1
    if i < j:
      l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data
    else:
      l.index(i).data, l.index(pivot).data = l.index(pivot).data, l.index(i).data
      break    
  return i

def partitionMid( l, low, high ): # pivot mid
  i, j, pivot = low, high-1, (low+high)//2

  l.index(high).data, l.index(pivot).data = l.index(pivot).data, l.index(high).data
  pivot = high
  
  while True:
    while l.index(i).data < l.index(pivot).data:
      i += 1
    while l.index(j).data > l.index(pivot).data:
      if j <= 0:
        break
      j -= 1
    if i < j:
      l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data
    else:
      l.index(i).data, l.index(pivot).data = l.index(pivot).data, l.index(i).data
      break  
    
  return i

def partitionFirst( l, low, high ): # pivot first
  i, j, pivot = low+1, high, low
  count = 0

  while True:
    if i < len(l)-1:
      while l.index(i).data < l.index(pivot).data:
        i += 1
        count += 1
    while l.index(j).data > l.index(pivot).data:
      j -= 1
      count += 1
    if i < j:
      l.index(i).data, l.index(j).data = l.index(j).data, l.index(i).data
      count += 1
    else:
      l.index(j).data, l.index(pivot).data = l.index(pivot).data, l.index(j).data
      count += 1
      break    
  return i, count
  



# ? LINKED LIST
class LinkedList:

  class Node:
    def __init__( self, data, next=None ):
      self.data = data
      self.next = next
    
    def __str__( self ):
      return str(self.data)
    
    
  def __init__( self ):
    self.head = self.Node(None)
  
  def __str__( self ):
    linked_data = ''
    p = self.head.next
    while p is not None:
      linked_data += str(p.data)
      linked_data += ' -> ' if p.next is not None else ''
      p = p.next
    return linked_data
  
  def __len__( self ):
    p = self.head.next
    count = 0
    while p is not None:
      count += 1
      p = p.next
    return count
  
  def index( self, i ):
    p = self.head.next
    for _ in range(i):
      if p.next is not None:
        p = p.next
      else:
        return None
    return p
  
  def append( self, data ):
    p = self.head
    while p.next is not None:
      p = p.next
    new_node = self.Node(data)
    p.next = new_node
  
  def removeHead( self ):
    deleted = self.head.next
    if deleted is not None:
      self.head.next = deleted.next
    return deleted