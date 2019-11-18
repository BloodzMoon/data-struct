
from Sort import *

data = [4,3,2,1,4,5,7,2]
ll = LinkedList()
for ele in data:
  ll.append(ele)

# bubbleSort(ll)
# selectionSort(ll)
# insertionSort(ll)
shellSort(ll)
# mergeSort(ll)
# quickSort(ll)
print(ll)
