
from Sort import *

data = [2,1,4,3]
# data = [4,3,2,1,5,4,7,2]
# data = []
# for i in range(21):
#   data.append(i)
ll = LinkedList()
for ele in data:
  ll.append(ele)

# bubbleSort(ll)
selectionSort(ll)
# insertionSort(ll)
# shellSort(ll)
# mergeSort(ll)
# print('count=',quickSort(ll))
print(ll)
