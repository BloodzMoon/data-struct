
class Node:

  def __init__( self, data, left=None, right=None ):
    self.data = data
    self.left = left
    self.right = right
    
  def __str__( self ):
    return str(self.data)

class BST:

  def __init__( self ):
    self.root = None

  def addI( self, data ):
    if self.root is None:
      self.root = Node(data)
    else:
      fp = None
      p = self.root
      while p is not None:
        fp = p
        p = p.left if data < p.data else p.right
      if data < fp.data:
        fp.left = Node(data)
      else:
        fp.right = Node(data)
  
  def add( self, data ):
    self.root = BST._add(self.root, data)
  
  def _add( root, data ):
    if root is None:
      return Node(data)
    else:
      if data < root.data:
        root.left = BST._add(root.left, data)
      else:
        root.right = BST._add(root.right, data)
      return root

  def inOrder( self ):
    BST._inOrder(self.root)
    print()
  
  def _inOrder( root ):
    if root is not None:
      BST._inOrder(root.left)
      print(root.data, end=' ')
      BST._inOrder(root.right)

  def preOrder( self ):
    BST._preOrder(self.root)
    print()

  def _preOrder( root ):
    if root is not None:
      print(root.data, end=' ')
      BST._preOrder(root.left)
      BST._preOrder(root.right)
    
  def postOrder( self ):
    BST._postOrder(self.root)
    print()
  
  def _postOrder( root ):
    if root is not None:
      BST._preOrder(root.left)
      BST._preOrder(root.right)
      print(root.data, end=' ')

  def printSideway( self ):         
    BST._printSideway(self.root, 0)         
    print() 
 
  def _printSideway( root, level ):         
    if root is not None:
      BST._printSideway(root.right, level+1)
      print('   '*level, root.data, sep='' )
      BST._printSideway(root.left, level+1)

  def search( self, data ):
    return BST._search(self.root, data)
  
  def _search( root, data ):
    if root is not None:
      if data < root.data:
        return BST._search(root.left, data)
      elif data > root.data:
        return BST._search(root.right, data)
      elif data == root.data:
        return root
  
  def path( self, data ):
    return BST._path(self.root, data, [])
  
  def _path( root, data, l ):
    if root is not None:
      l.append(root.data)
      if data < root.data:
        return BST._path(root.left, data, l)
      elif data > root.data:
        return BST._path(root.right, data, l)
      elif data == root.data:
        s = ''
        while len(l) is not 0:
          s = s + str(l.pop(0))
          s += '' if len(l) is 0 else ' -> '
        return s

  def maxRoot( root ):
    cur = root
    while cur.right is not None:
      cur = cur.right
    return cur

  def minRoot( root ):
    cur = root
    while cur.left is not None:
      cur = cur.left
    return cur

  def before( self, data ):
    prev, cur = None, self.root
    while cur is not None:
      if data == cur.data:
        return prev
      else:
        prev = cur
        cur = cur.left if data < cur.data else cur.right
    return prev

  def beforeOrder( self, data ):
    tmp = self.search(data)
    if tmp is not None and tmp.left is not None:
      tmp = BST.maxRoot(tmp.left)
      return tmp
    else:
      return None


  def deletedS( self, data ):
    return BST._deleteS(self.root, data)

  def _deleteS( root, data ): 
    if root is not None: 
      if data < root.data: 
        root.left = BST._deleteS(root.left, data) 
      elif data > root.data: 
        root.right = BST._deleteS(root.right, data) 
      else: 
        # Node with only one child or no child 
        if root.left is None: 
          temp = root.right  
          root = None 
          return temp  
        elif root.right is None: 
          temp = root.left  
          root = None
          return temp 
        # Node with 2 childs
        temp = BST.minRoot(root.right) 
        root.data = temp.data 
        root.right = BST._deleteS(root.right , temp.data) 
      return root  

  def deleteP( self, data ):
    return BST._deleteP(self.root, data)
  
  def _deleteP( root, data ):
    if root is not None:
      if data < root.data:
        root.left = BST._deleteP(root.left, data)
      elif data > root.data:
        root.right = BST._deleteP(root.right, data)
      else:
        # Node with only one child or no child 
        if root.left is None: 
          temp = root.right  
          root = None 
          return temp  
        elif root.right is None: 
          temp = root.left  
          root = None
          return temp 
        # Node with 2 childs
        temp = BST.maxRoot(root.left) 
        root.data = temp.data 
        root.left =   BST._deleteS(root.left , temp.data) 
      return root  




    

  