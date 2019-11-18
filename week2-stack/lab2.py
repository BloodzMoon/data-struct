
# ! Function #


def notMatch(last, i):
  if last is '(' and i is ')':
    return False
  elif last is '{' and i is '}':
    return False
  elif last is '[' and i is ']':
    return False
  else: return True


def myCheck(eq):
  keep = []
  error = False
  for i in eq:
    if i is '(' or i is '{' or i is '[':
      keep.append(i)
    elif i is ')' or i is '}' or i is ']':
      if len(keep) is 0:
        error = True
      else:
        last = keep.pop()
        if notMatch(last, i):
          error = True
  if error:
    print('Not Match')
  else: 
    print('Match')



# ! Main #
equation = str(input())
myCheck(equation)