
def factorial( n ):
  result = 1
  for i in range (1, n+1):
    result *= i
  return result


def multiples_of_3_and_5( n ):
  result = 0
  for i in range (1, n):
    if i % 3 == 0 or i % 5 == 0:
      result += i
  return result


def integer_right_triangles(p):
    result = []
    for a in range (p):
        for b in range (p):
            c = p - a - b
            if a <= b < c and c**2 == a**2 + b**2:
                result.append((a, b, c))
    return result

# straight forward but not good
def gen_pattern(chars):
    for line in range (1, len(chars)+1):
        text = ''
        for i in range (len(chars)-1, len(chars)-1-line, -1):
            text += chars[i]
        for i in range (len(text)-2, -1, -1):
            text += text[i]
        dot = '.'.join(text)
        pattern = dot.center(len(chars)*4-3, '.')
        print(pattern)

    for line in range (len(chars)-1, 0, -1):
        text = ''
        for i in range (len(chars)-1, len(chars)-1-line, -1):
            text += chars[i]
        for i in range (len(text)-2, -1, -1):
            text += text[i]
        dot = '.'.join(text)
        pattern = dot.center(len(chars)*4-3, '.')
        print(pattern)
    return 



#* MAIN 

# print( factorial( int(input('4.1 Enter integer: ')) ))
# print( multiples_of_3_and_5( int(input('4.2 Enter integer: ')) ))
# print( integer_right_triangles( int(input('4.3 Enter integer: ')) ) )
# gen_pattern(input('4.4 Enter string: '))
