
from Class import *

l = [int(e) for e in input("insert integers : ").split()] 
 
t = BST() 
for ele in l:     
  t.add(ele) 
 
 # 14 4 9 7 15 3 18 16 20 5 16
 # 5 3 2 4 7 6 8
 # 3 2 12 1 7 17 5 11 13 19 4 6 9 15 18 20
t.inOrder()
t.preOrder()
t.postOrder()
t.printSideway()
print('search :', t.search(7))
print('path :', t.path(16))
print('before :',t.before(7))
print('before order :',t.beforeOrder(16))
# t.deletedS(7)
t.deletedS(15)
print('\n\n\n\n\n')
t.printSideway()