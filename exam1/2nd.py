
from Class import LinkedList

def calMean( ll ):
  sum = 0
  count = 0
  p = ll.head.next
  while p is not None:
    sum += p.data
    count += 1
    p = p.next
  return sum / count

def calMode( ll ):
  l = []
  p = ll.head.next
  while p is not None:
    l.append(p.data)
    p = p.next
  
  modes = []
  maxCount =  max(map(l.count, l))
  for i in l:
    if l.count(i) == maxCount:
      modes.append(i)
  modes = list(dict.fromkeys(modes))
  return modes

def calMedian( ll ):
  l = []
  count = 0
  p = ll.head.next
  while p is not None:
    l.append(p.data)
    count += 1
    p = p.next

  return l[count//2] if count % 2 != 0 else (l[(count//2)-1] + l[(count//2)]) / 2


### ! Main ###
ll = LinkedList()

number = list(map(int, input('Enter 12 number : ').split()))
for i in number:
  ll.add(i)
print('Output :')
print('LinkedList data : ', ll)
print('Mean = {0:.2f}'.format(calMean(ll)))
print('Mode = ', calMode(ll))
print('Median = {0:.2f}'.format(calMedian(ll)))