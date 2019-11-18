
def factorOf( number, f=2 ):
  if f <= number:
    if number % f == 0:
      print(f, end=' ')
      factorOf(number/f)
    else:
      factorOf(number, f+1)


# ! MAIN
factorOf(70)