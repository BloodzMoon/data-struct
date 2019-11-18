
class Stack:
  def __init__( self, items=None ):
    self.items = [] if items is None else items

  def __str__( self ):
    return str(self.items)

  def __len__( self ):
    return len(self.items)
  
  def isEmpty( self ):
    return len(self) == 0
  
  def push( self, new_item ):
    self.items.append(new_item)
  
  def pop( self ):
    return self.items.pop()

  def peek( self ):
    return self.items[-1] if not self.isEmpty() else None




class Queue:
  def __init__( self, items=None ):
    self.items = [] if items is None else items
  
  def __str__( self ):
    return str(self.items)

  def __len__( self ):
    return len(self.items)

  def enqueue( self, new_item ):
    self.items.append(new_item)
  
  def dequeue( self ):
    return self.items.pop(0)

  def isEmpty( self ):
    return len(self) == 0




class LinkedList:

  class Node:
    def __init__( self, data, next=None ):
      self.data = data
      self.next = next
  
  def __init__( self ):
    self.head = self.tail = self.Node(None)

  def __str__( self ):
    l = []
    p = self.head.next
    while p is not None:
      l.append(p.data)
      p = p.next
    return str(l)
  
  def __len__( self ):
    size = 0
    p = self.head.next
    while p is not None:
      size += 1
      p = p.next
    return size
  
  def isEmpty( self ):
    return len(self) == 0

  def append( self, data ):
    new_node = self.Node(data)
    self.tail.next = new_node
    self.tail = new_node
  
  def getNode( self, data ):
    p = self.head.next
    while p is not None:
      if p.data == data:
        return p
      p = p.next

  def before( self, data ):
    p = self.head
    while p.next is not None:
      if p.next.data == data:
        return p
      p = p.next

  def remove( self, data ):
    if self.getNode(data) is not None:
      removed_node = self.getNode(data)
      self.before(data).next = removed_node.next
      return removed_node
  
  # order linkedlist
  def add( self, data ):
    if self.isEmpty():
      self.append(data)
    else:
      p = self.head.next
      while p is not None:
        if data <= p.data:
          new_node = self.Node(data)
          new_node.next = p
          self.before(p.data).next = new_node
          return
        p = p.next
      self.append(data)