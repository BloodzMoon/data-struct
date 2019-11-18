

from Class import Stack

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


def postTOin( postfix ):
  s = Stack()
  infix = ''
  for c in postfix:
    if checkType(c) == 'operand':
      s.push(c)
    elif checkType(c) == 'operation':
      tmp_b = s.pop()
      tmp_a = s.pop()
      tmp = '(' + tmp_a + c + tmp_b + ')'
      s.push(tmp)
  while not s.isEmpty():
    infix += s.pop()
  return infix



### ! Main ###

while True:
  print('\n\n\n\n\n\n\n\n\n\n')

  postfix = input('Enter postfix expression    : ')
  l = postTOin(postfix)
  print('Result infix expression :', l)

  inpt = input('\nTry again? y/n : ')
  if inpt == 'y':
    print('\n\n\n\n\n\n\n\n\n\n')
  else:
    break
