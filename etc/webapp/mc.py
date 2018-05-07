#!/usr/bin/python3.6

# MEMCACHE

from debug import test_iterator

class Memcache():
  def __init__(self):
    self.CACHE = {}

  def set(self,key,value):
    # Check there are no duplicates?
    self.CACHE[key] = value
    print('Cache set key:',key,' value:',value)
    return None

  def get(self,key):
    return self.CACHE[key]

  def delete(self,key):
    if key in self.CACHE:
      del self.CACHE[key]
      print('Cache delete key:',key)
    else:
      print('Key in found in CACHE.')

  def flush(self):
    # Clear everything in dictionary
    self.CACHE.clear()
    print('MEMCACHE cleared!')
    return None

def test_memcache():
  print(test_memcache.__name__)
  m = Memcache()
  print(m.set('a','1'))
  print(m.set('b','2'))
  print(m.CACHE)
  print(m.get('b'))
  m.delete('b')
  print(m.CACHE)
  m.flush() # Not working
  print(m.CACHE)

if __name__ == '__main__':
  cache = Memcache()
  test_iterator(cache)

