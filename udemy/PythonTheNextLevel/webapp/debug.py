#!/usr/env/python3.6

# DEBUG
# import into python code for debugging purposes

def test_iterator(object):
  try:
    cache_iterator = iter(object)
  except:
    print(object,' is not iterable!')

