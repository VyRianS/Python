#!/usr/bin/python3.6

# Load Balancer
# Looping through servers in order

import itertools
import c1
import c2
import c3

## Server names
SERVERS = [c1,c2,c3]
server_index = 0

#def get_server_iter():
#  global cycle
#  return next(cycle)

#def get_server():
  # Return server name
  # Add code to PING server to check they are up
#  global server_index # Tell function that server_index is global, or else next line will have scope error
#  global SERVERS
#  target_server = SERVERS[server_index]
#  if server_index == len(SERVERS)-1:
#   server_index = 0
#  else:
#    server_index += 1
#  return target_server
  
def get_server():
  try:
    return next(get_server.s)
  except StopIteration:
    get_server.s=iter(SERVERS)
    return next(get_server.s)

setattr(get_server,'s',iter(SERVERS))

if __name__ == "__main__":
  from random import randint
  # Simulate number of requests with loop
  for i in range(10):
    a = randint(5,99)
    b = randint(5,99)
    
    # Get host from load balancer
    server = get_server()

    print('Host:',server.printName())
    print('Latest result:',server.multiplyHandler(a,b))
    print('Last 5 results:',server.lastMultipliedHandler())
    print("")
 
