
class Node:

  def __init__( self, data, next=None , prev=None):
    self.data = data
    self.next = next
    self.prev = prev

  def __str__( self ):
    return str(self.data)

  def getData( self ):
    return self.data

  def getNext( self ):
    return self.next
  
  def getPrev( self ):
    return self.prev

  def setData( self, data ):
    self.data = data
  
  def setNext( self, next ):
    self.next = next

  def setPrev( self, prev ):
    self.prev = prev