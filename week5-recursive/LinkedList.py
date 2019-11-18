
from Node import *

class LinkedList:

  # constructor
  def __init__( self ):
    self.head = None
    self.tail = None

  # to string
  def __str__( self ):
    if self.isEmpty():
      return 'Empty->Linked->List'
    else:
      linked_data = ''
      p = self.head

      while p is not None:
        linked_data += str(p.getData())
        linked_data += ' -> ' if p.getNext() is not None else ''
        p = p.getNext()
        
      linked_data = 'Size: ' + str(self.size()) + '\n' + linked_data
      return linked_data
      
  # functions
  def size( self ):
    p = self.head
    count = 0
    while p is not None:
      count += 1
      p = p.getNext()
    return count
  
  def isEmpty( self ):
    return self.size() is 0

  def addHead( self, data ):
    if len(data) is not 0:
      if self.isEmpty():
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
      else:
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head.setPrev(new_node)
        self.head = new_node
  
  def append( self, data ):
    if str(data) != 's':
      if self.isEmpty():
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
      else:
        new_node = Node(data)
        new_node.setPrev(self.tail)
        self.tail.setNext(new_node)
        self.tail = new_node
      
  def isIn( self, data ):
    p = self.head
    while p is not None:
      if str(p.getData()) == str(data):
        return True
      else:
        p = p.getNext()
    return False
  
  def before( self, data ):
    p = self.head
    while p is not None:
      if str(p.getData()) == str(data):
        return None if p.getPrev() is None else p.getPrev()
      else:
        p = p.getNext()
    return None

  def remove( self, data ):
    p = self.head
    while p is not None:
      if str(p.getData()) == str(data):

        # X current X
        if p.getPrev() is None and p.getNext() is None: 
          self.head = None
          self.tail = None
        # data current X
        elif p.getPrev() is not None and p.getNext() is None:
          self.tail = p.getPrev()
          self.tail.setNext(None)
          p.setPrev(None)
        # X current data
        elif p.getPrev() is None and p.getNext() is not None:
          self.head = p.getNext()
          self.head.setPrev(None)
          p.setNext(None)
        # data current data
        else:
          p.getPrev().setNext(p.getNext())
          p.getNext().setPrev(p.getPrev())
          p.setNext(None)
          p.setPrev(None)

        return p
      else:
        p = p.getNext()
    return None

  def removeHead( self ):
    if not self.isEmpty():
      return self.remove(self.head.getData())
  
  def removeTail( self ):
    if not self.isEmpty():
      return self.remove(self.tail.getData())

  def bottomUp( self, percent ):
    if self.isEmpty() or percent >= 100 or percent <= 0:
      return
    count = int(self.size() * percent / 100)
    for i in range(count):
      removed_node = self.removeHead()
      self.append(removed_node.getData())

  def deBottomUp( self, percent ):
    if self.isEmpty() or percent >= 100 or percent <= 0:
      return
    count = int(self.size() * percent / 100)
    invert_count = self.size() - count
    for i in range(invert_count):
      removed_node = self.removeHead()
      self.append(removed_node.getData())  

  def riffle( self, percent ):
    # ignore case
    if self.isEmpty() or percent >= 100 or percent < self.size():
      return
    count = int(self.size() * percent / 100)
    if count is 0:
      return

    # split linked list into 2 linked list
    p = self.head
    for i in range(count):
      p = p.getNext()
    self.tail = p.getPrev()
    self.tail.setNext(None)
    tmp_head = p
    tmp_head.setPrev(None)

    # insert tmp_list into main_list (riffle)
    p_main = self.head
    p_tmp = tmp_head
    while p_tmp is not None:
      # store next item
      main_next = p_main.getNext()
      tmp_next = p_tmp.getNext()

      # insert link
      p_main.setNext(p_tmp)
      p_tmp.setPrev(p_main)
      if main_next is None:
        break
      else:
        p_tmp.setNext(main_next)
        main_next.setPrev(p_tmp)

      # move pointer then repeat
      p_main = main_next
      p_tmp = tmp_next
    
    # find new tail
    p = self.head
    while p.getNext() is not None:
      p = p.getNext()
    self.tail = p

  def deRiffle( self, percent ):
    # ignore case
    if self.isEmpty() or percent >= 100 or percent < self.size():
      return
    count = int(self.size() * percent / 100)
    if count is 0:
      return
    
    # fix bug each case
    if percent > 50:
      count = self.size() - count
      remaining = 0
    elif percent < 50:
      count -= 1
      remaining = self.size() - (count*2+1)
    elif percent == 50:
      if self.size() % 2 == 1:
        count -= 1
        remaining = self.size() - (count*2+1)
      else:
        remaining = 0

    # remove riffled node and append at the bottom of linked list
    p = self.head.getNext()
    for i in range(count):
      p_next = p.getNext()
      if p_next is None:
        break
      removed_node = self.remove(p.getData())
      self.append(removed_node.getData())
      p = p_next.getNext()
    
    # move remaining node to the bottom
    for i in range(remaining):
      p_next = p.getNext()
      if p_next is None:
        break
      removed_node = self.remove(p.getData())
      self.append(removed_node.getData())
      p = p_next

    # find new tail
    p = self.head
    while p.getNext() is not None:
      p = p.getNext()
    self.tail = p
