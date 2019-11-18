
def print90( ll, i=0, level=0 ):
  if i in range(len(ll)):
    # Right
    print90(ll, i*2+2, level+1)
    # Current
    print('    '*level, ll.index(i), sep='')
    # Left
    print90(ll, i*2+1, level+1)


def insertMin( ll, data ):
  ll.append(data)
  heapifyMin(ll)

def heapifyMin( ll, cur=None ):
  cur = len(ll)-1 if cur is None else cur
  before = int(cur//2 if cur % 2 == 1 else (cur/2)-1)
  if before in range(len(ll)):
    if ll.index(cur).data < ll.index(before).data:
      ll.index(cur).data, ll.index(before).data = ll.index(before).data, ll.index(cur).data
    heapifyMin(ll, before)
    # if len(ll) > 1:
    #   heapifyMin(ll[:len(ll)-1])

def deleteMin( ll, last=None, d=None, i=0 ):
  deleted = ll.index(i).data if d is None else d
  last = len(ll)-1 if last is None else last
  left = ll.index(i*2+1).data if i*2+1 <= last else None
  right = ll.index(i*2+2).data if i*2+2 <= last else None

  if right is None:
    if left is None:
      ll.index(last).data = deleted
      return deleted
    else:
      ll.index(i).data = left
      return deleteMin(ll, last, deleted, i*2+1)
  else:
    if left < right:
      ll.index(i).data = left
      return deleteMin(ll, last, deleted, i*2+1)
    else:
      ll.index(i).data = right
      return deleteMin(ll, last, deleted, i*2+2)
  
  
  


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

  
  
