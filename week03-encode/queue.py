
class Queue:

  # constructor
  def __init__( self, myQueue=None ):
    if myQueue is None:
      self.items = []
      self.MAX_SIZE = 4
    else:
      self.items = myQueue
      self.MAX_SIZE = len(myQueue)

  # functions
  def size( self ):
    return len(self.items)

  def isEmpty( self ):
    # return self.size() is 0
    return False
  
  def isFull( self ):
    # return self.size() is self.MAX_SIZE
    return False

  def enQueue( self, newItem ):
    if self.isFull():
      print('Queue Full!')
    else:
      self.items.append(newItem)

  def deQueue( self ):
    # if self.isEmpty():
    #   print('Queue Empty!')
    # else:
    return self.items.pop(0)


### Main ###
word = Queue()
code = Queue()
counter = 0

def asciiOver( c, shift ):
  if c >= 65 and c <= 90:
    c -= 65
    return chr(65 + ((c+shift) % 26))

  elif c >= 97 and c <= 122:
    c -= 97
    return chr(97 + ((c+shift) % 26))

def asciiLower( c, shift ):
  if c >= 65 and c <= 90:
    c -= 65
    return chr(90 - (25 - ((c-shift) % 26)))

  elif c >= 97 and c <= 122:
    c -= 97
    return chr(122 - (25 - ((c-shift) % 26)))


while True:
  print('<<<< Caesar Cipher >>>>')
  print('[1] Enter new word')
  print('[2] Encode')
  print('[3] Decode')
  print('[4] Exit')
  menu = input('select your menu >> ')

  if menu is '1':
    counter = 0
    inWord = input('word >> ')
    del word
    word = Queue()
    for i in inWord:
      word.enQueue(i)
    print('\n\t')
    print(''.join(word.items))
    print('\n')

  elif menu is '2':
    counter += 1
    inCode = input('encode >> ')
    del code
    code = Queue()
    for i in inCode:
      code.enQueue(i)
    
    for i in range(word.size()):
      tmpWord = word.deQueue()
      if tmpWord is ' ':
        word.enQueue( tmpWord )
      else:
        tmpCode = int(code.deQueue())
        # word.enQueue( chr(ord(tmpWord) + tmpCode) )
        word.enQueue( asciiOver(ord(tmpWord), tmpCode)) 
        code.enQueue(tmpCode)
    
    print('\n\t')
    print(''.join(word.items))
    print('\n')

  elif menu is '3':
    if counter is 0:
      print('* Nothing to decode')
    else:
      counter -= 1
      inCode = input('decode >> ')
      del code
      code = Queue()
      for i in inCode:
        code.enQueue(i)
      
      for i in range(word.size()):
        tmpWord = word.deQueue()
        if tmpWord is ' ':
          word.enQueue( tmpWord )
        else:
          tmpCode = int(code.deQueue())
          word.enQueue( asciiLower(ord(tmpWord), tmpCode) ) 
          code.enQueue(tmpCode)
    
    print('\n\t')
    print(''.join(word.items))
    print('\n')
  
  elif menu is '4':
    print('Good bye!')
    exit(0)

