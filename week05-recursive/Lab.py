
def eat( n ):
  if n is 1:
    print('eat', n)
  else:
    print('eat', n, end=' ')
    eat(n-1)

def fac( n ):
  if n is 1:
    return 1
  else:
    return n * fac(n-1)

def sum1ToN( n ):
  # minimal style
  return 1 if n is 1 else n + sum1ToN(n-1)

def printNto1( n ):
  if n is 1:
    print(n)
  else:
    print(n, end=' ')
    printNto1(n-1)
  
def print1ToN( n ):
  if n is 1:
    print(n, end=' ')
  else:
    print1ToN(n-1)
    print(n, end=' ')

def fib( n ):
  if n <= 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)

def binarySearch( lo, hi, x, l ):
  mid = int((lo + hi)/2)
  if l[mid] is x:
    return mid
  elif lo is hi:
    return None
  elif l[mid] > x:
    hi = mid-1
    return binarySearch(lo, hi, x, l)
  elif l[mid] < x:
    lo = mid+1
    return binarySearch(lo, hi, x, l)

# tower of hanoi
def move( n, src, dest ): 

  # base case
  if n is 1:
    print('Move', src, 'to', dest)
  
  # BIGGER case
  else:
    l = ['A', 'B', 'C']
    s = l.pop(l.index(src))
    d = l.pop(l.index(dest))
    keep = l.pop()

    move(n-1, s, keep)
    print('Move', s, 'to', d)
    move(n-1, keep, d)
    

def sum1( n, l ):
  if n is 1:
    return l[0]
  else:
    return l[n-1] + sum1(n-1, l)

def sum2( n, l, i=0 ):
  if i is n-1:
    return l[i]
  else:
    return l[i] + sum2(n, l, i+1)

def sum3( l, i=0 ):
  if len(l) is 1:
    return l[0]
  else:
    return l[i] + sum3(l[i+1:])

def printlistForw( l, i=0 ):
  if len(l) is 1:
    print(l[0])
  else:
    print(l[i], end=' ')
    printlistForw(l[i+1:])

def printlistBkw( l, i=0 ):
  if len(l) is 1:
    print(l[0], end=' ')
  else:
    printlistBkw(l[i+1:])
    print(l[i], end=' ')

def app( n, l, i=1 ):
  if i is n:
    l.append(n)
  else:
    l.append(i)
    app(n, l, i+1)

def appB( n, l ):
  if n is 1:
    l.append(1)
  else:
    l.append(n)
    appB(n-1, l)

from LinkedList import *
def printList( ll, p=None ):
  if p is None:
    p = ll.head
    printList(ll,p)
  elif p.getNext() is None:
    print(p.getData())
  else:
    print(p.getData(), end='->')
    printList(ll, p.getNext())

def createLLL(l, i=0, ll=None):
  if ll is None:
    ll = LinkedList()
    createLLL(l, i, ll)
    return ll
  elif len(l) is 1:
    ll.append(l[i])
  else:
    ll.append(l[i])
    createLLL(l[i+1:], i, ll)

def createLL(n, i=1, ll=None):
  if ll is None:
    ll = LinkedList()
    createLL(n, i, ll)
    return ll
  elif i is n:
    ll.append(n)
  else:
    ll.append(i)
    createLL(n, i+1, ll)

#! Main ###

eat(5)

print('factorail:', fac(5))

print('sum:', sum1ToN(100))

printNto1(5)

print1ToN(5)
print('')

print('fibonaci:', fib(7))

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('binary search index: ' + str(binarySearch(0, len(list1)-1, 7, list1)))

move(3, 'A', 'C')

list2 = [7, 3, 5, 4, 2, 6, 8, 9, 1]
print('sum1: ', sum1(len(list2), list2))

print('sum2: ', sum2(len(list2), list2))

print('sum3: ', sum3(list2))

printlistForw(list1)

printlistBkw(list1)
print('')

list3 = []
app(7, list3)
print('app: ', list3)

list4 = []
appB(7, list4)
print('app: ', list4)

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(6)
linked_list.append('z')
printList(linked_list)

list5 = ['A', 'B', 'C', 'D']
linked_list2 = createLLL(list5)
printList(linked_list2)

linked_list3 = createLL(5)
printList(linked_list3)


