
class Node:
  def __init__( self , data, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
  
  def __str__( self ):
    return str(self.data)


def print90( root, level=0 ):
  if root is not None:
    print90(root.right, level+1)
    print('    '*level, root.data)
    print90(root.left, level+1)

def add( root, data ):
  if root is None:
    return Node(data)
  else:
    if data < root.data:
      root.left = add(root.left, data)
    else:
      root.right = add(root.right, data)
    return root

def search( root, data ):
  if root is not None:
    if data < root.data:
      return search(root.left, data)
    elif data > root.data:
      return search(root.right, data)
    else:
      return root

def before( root, data ):
  be = None
  cur = root
  while cur is not None:
    if data == cur.data:
      return be
    else:
      be = cur
      cur = cur.left if data < cur.data else cur.right

# TODO NEW PATH[***]
def path( root, data ):
  return ' -> '.join(RootToNode(root, data))

def depth( root, data ):
  if search(root, data) is not None:
    if data < root.data:
      return 1 + depth(root.left, data)
    elif data > root.data:
      return 1 + depth(root.right, data)
    else:
      return 0

def minRoot( root ):
  p = root
  while p.left is not None:
    p = p.left
  return p

def maxRoot( root ):
  p = root
  while p.right is not None:
    p = p.right
  return p


# TODO DELETE [***]
def del_S( root, data ):
  if root is not None:
    if data < root.data:
      root.left = del_S(root.left, data)
    elif data > root.data:
      root.right = del_S(root.right, data)
    else:
      if root.left is None:
        tmp = root.right
        root = None
        return tmp
      if root.right is None:
        tmp = root.left
        root = None
        return tmp
      
      # * DIFFERENT FROM P [***]
      tmp = minRoot(root.right) 
      root.data = tmp.data
      root.right = del_S(root.right, tmp.data)
    return root

def del_P( root, data ):
  if root is not None:
    if data < root.data:
      root.left = del_P(root.left, data)
    elif data > root.data:
      root.right = del_P(root.right, data)
    else:
      if root.left is None:
        tmp = root.right
        root = None
        return tmp
      if root.right is None:
        tmp = root.left
        root = None
        return tmp
      
      # * DIFFERENT FROM S [***]
      tmp = maxRoot(root.left) 
      root.data = tmp.data
      root.left = del_S(root.left, tmp.data)
    return root


# TODO * New function *
def pathAtoB( root, A, B ):
  a = search(root, A)
  b = search(root, B)
  if a is not None and b is not None:
    return ' -> '.join(NodeToNode(root, A, B))

def NodeToNode( root, A, B ):
  a = search(root, A)
  b = search(root, B)
  if a is not None and b is not None:
    # *find the junction root
    while True:
      if a.data < root.data and b.data < root.data:
        root = root.left
      elif a.data > root.data and b.data > root.data:
        root = root.right
      else:
        break
    
    tmp1 = NodeToRoot(root, a.data)
    tmp2 = RootToNode(root, b.data) 
    result = []
    result += tmp1
    result += tmp2 
    result = list(dict.fromkeys(result))
    return result 

def RootToNode( root, data, l=None ):
  l = [] if l is None else l
  if root is not None:
    l.append(str(root.data))
    if data < root.data:
      return RootToNode(root.left, data, l)
    elif data > root.data:
      return RootToNode(root.right, data, l)
    else:
      return l

def NodeToRoot( root, data ):
  if root is not None:
    tmp = RootToNode(root, data)
    if tmp is not None:
      tmp.reverse()
      return tmp

def diffAtoB( root, A, B ): # different depth
  a = depth(root, A)
  b = depth(root, B)
  if a is not None and b is not None:
    return abs(a-b)

def howFarAtoB( root, A, B ): # count jump betweem A to B
  return len(NodeToNode(root, A, B))-1



# ! MAIN
r = None
for _ in [15, 10, 20, 13, 7, 17, 23, 11, 14]:
  r = add(r, _)

# print90(r)
# print(pathAtoB(r, 11, 23))

# try other funtions
print(' * '.join(['a', 'c', 'b']))
