

from Class import Stack

def isLessOrEqualPriority( cur, prev ):
  c_priority = 1 if cur in ['+', '-'] else 2 
  p_priority = 1 if prev in ['+', '-'] else 2
  return c_priority <= p_priority
  

def checkType( c ):
  if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
    return 'operand'
  elif c in ['+', '-', '*', '/']:
    return 'operation'
  elif c == '(':
    return 'open-parenthesis'
  elif c == ')':
    return 'close-parenthesis'
  else:
    return 'error'


def inTOpost( infix ):
  s = Stack()
  postfix = ''
  operation = 0
  operand = 0
  
  for c in infix:
    if checkType(c) == 'operand':
      operand += 1
      postfix += c
    else:
      if checkType(c) == 'open-parenthesis':
        s.push(c)
      elif checkType(c) == 'close-parenthesis':
        while not s.isEmpty():
          if s.peek() == '(':
            s.pop()
            break
          postfix += s.pop()
      elif checkType(c) == 'operation':
        operation += 1
        while not s.isEmpty() and isLessOrEqualPriority(c, s.peek()):
            if s.peek() == '(':
              break
            postfix += s.pop()
        s.push(c)

  while not s.isEmpty():
    postfix += s.pop()

  return postfix, operation, operand


def inTOpre( infix ):
  reversed_infix = ''
  tmp = infix[::-1]
  for c in tmp:
    if c == '(':
      reversed_infix += ')' 
    elif c == ')':
      reversed_infix += '(' 
    else:
      reversed_infix += c 
  result = inTOpost(reversed_infix)
  prefix = result[0]
  prefix = prefix[::-1]
  return prefix



### ! Main ###

while True:
  print('\n\n\n\n\n\n\n\n\n\n')

  infix = input('Enter infix expression    : ')
  l = inTOpre(infix)
  print('Result prefix expression :', l)

  inpt = input('\nTry again? y/n : ')
  if inpt == 'y':
    print('\n\n\n\n\n\n\n\n\n\n')
  else:
    break
