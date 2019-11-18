
class Node:

  def __init__( self, data, left=None, right=None ):
    self.data = data
    self.left = left
    self.right = right
  
  def __str__( self ):
    return str(self.data)


def addi( root, data ):
  if root is None:
    return Node(data)
  else:
    if data < root.data:
      root.left = addi(root.left, data)
    else:
      root.right = addi(root.right, data)
    return root

def inOrder( root ):
  if root is not None:
    inOrder(root.left)
    print(root.data, end=' ')
    inOrder(root.right)
 
def printSideway( root, level ):       
  if root is not None:
    printSideway(root.right, level + 1)
    print('   ' * level, root.data, sep='')
    printSideway(root.left, level + 1)

def height( root, level=0 ):
  if root is not None:
    a = height(root.right, level + 1)
    b = height(root.left, level + 1)
    return max(a, b)
  else:
    return level - 1 

def path( root, data, l=[] ):
  if root is not None:
    l.append(root.data)
    if data < root.data:
      path(root.left, data, l)
    elif data > root.data:
      path(root.right, data, l)
    elif data == root.data:
      s = ''
      while len(l) is not 0:
        s = s + str(l.pop(0)) + ' '
      print(s)

def search( root, data ):
  if root is not None:
    if data < root.data:
      return search(root.left, data)
    elif data > root.data:
      return search(root.right, data)
    elif data == root.data:
      return root
        
def depth( root, data, level=0 ):
  if root is not None:
    if data < root.data:
      return depth(root.left, data, level + 1)
    elif data > root.data:
      return depth(root.right, data, level + 1)
    elif data == root.data:
      return level

def father( root, data ):
  prev, cur = None, root
  while cur is not None:
    if data == cur.data:
      return prev
    else:
      prev = cur
      cur = cur.left if data < cur.data else cur.right
  return prev

def minRoot( root ):
  cur = root
  while cur.left is not None:
    cur = cur.left
  return cur