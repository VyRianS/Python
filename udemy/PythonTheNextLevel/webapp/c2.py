#!/usr/bin/python3.6

import db
from mc import Memcache

rlist = []
cache = Memcache()

def printName():
  return str(__name__)

def updateLastFive(result):
  key = 'LastFive'
  lastlist = cache.get(key)
  # Check if list is already full
  if len(lastlist) >= 5:
    newlist = lastlist[1:]
    newlist.append(result)
    cache.set(key,newlist)
  else:
    # Length of list is less than 5, just append
    lastlist.append(result)
    cache.set(key,lastlist)

def lastMultipliedHandler():
  return cache.get('LastFive')

def multiplyHandler(a,b):
  # Output results from db.py (Russian peasant's algo)
  key = (a,b)
  # Add to result list
  if key in cache:
    cache.get(key)
  else:
    result = db.rpm(a,b)
    cache.set(key,result)
  return result

# if this script is called via ./cX.py
if __name__ == "__main__":
  multiplyHandler(2,4)
  multiplyHandler(357,16)
  multiplyHandler(24,16)
  multiplyHandler(17,86)
  multiplyHandler(210,87)
  multiplyHandler(90,3686)
  lastMultipliedHandler()
