
from LinkedList import *
import msvcrt as m


l = LinkedList()

while True:
  print(chr(27) + "[2J") # << CLEAR SCREEN

  print('[ Linked->List ]\n')
  print(l, end='\n\n')
  print('❤  1.Add Head')
  print('✨  2.Add Tail')
  print('🗑  3.Remove Head ')
  print('❄  4.Remove Tail')
  print('❌  5.Remove...')
  print('⚠  6.Reset')
  print('⚔  7.Scramble')
  print('✈  8.Exit')
  print('Select menu -> ')
  menu =  m.getwch() 

  if menu is '1':
    print('Adding head.. -> ')
    data = m.getwch()
    l.addHead(data)
  elif menu is '2':
    print('Adding tail.. -> ')
    data = m.getwch()
    l.append(data)
  elif menu is '3':
    l.removeHead()
  elif menu is '4':
    l.removeTail()
  elif menu is '5':
    print('Removing.. -> ')
    data = m.getwch()
    l.remove(data)
  elif menu is '6':
    del l
    l = LinkedList()
  elif menu is '7':

    while True:
      print(chr(27) + "[2J") # << CLEAR SCREEN
      print('[ Scramble->Linked->List ]\n')
      print(l, end='\n\n')
      print('⚜  1.Bottom Up')
      print('➰  2.Riffle')
      print('⚓  3.De-Bottom up')
      print('♨  4.De-Riffle')
      print('✈  5.Back\n')  
      print('Select menu -> ')
      menu =  m.getwch() 

      if menu is '1':
        percent = input('Bottom up %.. -> ')
        l.bottomUp(int(percent))
      elif menu is '2':
        percent = input('Riffle %.. -> ')
        l.riffle(int(percent))
      elif menu is '3':
        percent = input('De-Bottom %.. -> ')
        l.deBottomUp(int(percent))
      elif menu is '4':
        percent = input('De-Riffle %.. -> ')
        l.deRiffle(int(percent))
      elif menu is '5':
        break

  elif menu is '8':
    print(chr(27) + "[2J") # << CLEAR SCREEN
    print('Goodbye!')
    exit(0)
    
  elif menu is '*':
    integer = 1
    for i in range(10):
      l.append(str(integer))
      integer += 1