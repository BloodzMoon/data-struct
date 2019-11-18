
from Class import *

l = [14,4,9,7,15,3,18,16,20,5,16]

r = None
for e in l:
  r = addi(r, e)

print('inOrder: ', end='')
inOrder(r)
print()

print('printSideWay')
printSideway(r, 0)

print('height of ', r.data, '=', height(r))

d = 5
print('path: ', d, '=', end=' ')
path(r, d)

d = 9
print(search(r, d))

d = 14
print('father of', d, 'is', father(r, d))


d = 18
print('depth of node data', d, '=', depth(r, d))

print('smallest data =', minRoot(r))