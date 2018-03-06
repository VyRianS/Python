#!/usr/bin/python3.6

# Russian Peasant Multiplication
# http://mathforum.org/dr.math/faq/faq.peasant.html

import time
from mc import Memcache

# Caching the results to improve performance
CACHE = {}

def rpm(x,y):
  key = (x,y)
  if key in CACHE:
    total = CACHE[key]
    print('CACHE HIT')
  else:
    decr = x
    incr = y
    total = 0
    while decr >= 1:
      if int(decr) % 2 == 1:
        total = total + incr
      decr = decr/2
      incr = incr*2
    CACHE[key] = total
    print('DB Hit')
  return total

def run_rpm():

  start_time = time.time()
  print(rpm(357,16))
  print("rpm() took %f seconds" % (time.time()-start_time))

if __name__ == "__main__":
  run_rpm()

"""
MODEL ANSWER

def russian(a,b):
  x = a; y = b; z = 0
  while x > 0:
    if x % 2 == 1: z = z + y
    y = y << 1 # Shift binary to left by 1 position, divide by 2
    x = x >> 1 # Shift binary to right by 1 position, multiply by 2
  return z
"""
