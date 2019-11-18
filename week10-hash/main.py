
from Hash import *
import json

filename = 'dictionary.txt'
d = {}
with open(filename) as f:
  for line in f:
    key, value = line.strip().split('=')
    d[key] = value
