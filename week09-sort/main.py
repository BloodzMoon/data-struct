
from Heap import *

heap = LinkedList()
l = [68, 65, 32, 24, 26, 21, 19, 13, 16, 14]
# l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

for e in l:
  print('insert', e)
  insertMin(heap, e)
  print(heap)
  print90(heap)
  print('----------')


a = []
print('\nDELETED!')
for i in reversed(range(1, len(heap))):
  last = heap.index(i)
  tmp = deleteMin(heap, i)
  print('deleteMin', tmp, 'FindPlaceFor', last)
  print(heap)
  print90(heap)
  print('----------')
  a.append(tmp)


print('Sorting', a)