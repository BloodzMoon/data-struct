
class Stack:

  def __init__(self, myList=None):
    self.items = [] if myList is None else myList
    self.SIZE = len(self.items)

  def size(self):
    return self.SIZE

  def isEmpty(self):
    return self.SIZE == 0

  def pop(self):
    return self.items.pop()

  def peek(self):
    return self.items[-1]



l = Stack(['a', 'b', 'c'])
print(l.pop())
print(l.size())