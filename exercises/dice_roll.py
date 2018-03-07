#!/usr/bin/python3.6

# DICE ROLLING SIMULATOR

import random

ROUND = 0
MIN_ROLL = 1
MAX_ROLL = 99
LAST_RESULT = []
MAX_RECORD_LEN = 10

def display_dice(min_roll, max_roll):
  print('Simulating a', max_roll, 'sided dice ...')
  print('MIN_ROLL =', min_roll, ' MAX_ROLL =', max_roll)

def display_last():
  print(LAST_RESULT)
  
def display_average():
  print('Last 10 average:',sum(LAST_RESULT)/float(len(LAST_RESULT)))

def roll_dice(min_roll, max_roll):
  global ROUND
  ROUND = ROUND + 1 
  result = random.randint(min_roll, max_roll)
  print('ROUND', ROUND, '- rolled', result)
  if len(LAST_RESULT) == MAX_RECORD_LEN:
    LAST_RESULT.pop(0) # Remove first item from list
  LAST_RESULT.append(result) # Append to the back of list
  return result

if __name__ == '__main__':
  display_dice(MIN_ROLL, MAX_ROLL)
  while True:
    roll_dice(MIN_ROLL, MAX_ROLL)
    display_last()
    display_average()

    # For Python3+ raw_input() has been renamed to input()
    user_input = input('Do you wish to continue? (Y/N) [Y] ')

    # If user input is empty, set to Y 
    if not user_input:
      user_input = 'Y'
 
    if user_input == 'N':
      break
    elif user_input != 'Y':
      print('Invalid input, exiting.')
      break

  print('Execution complete!')
 
