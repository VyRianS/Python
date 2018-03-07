#!/usr/bin/python3.6

# DICE ROLLING SIMULATOR

import random

MIN_ROLL = 1
MAX_ROLL = 6

def display_dice():
  print('MIN_ROLL =', MIN_ROLL, ' MAX_ROLL =', MAX_ROLL)

def roll_dice(min_roll,max_roll):
  return random.randint(min_roll,max_roll)

if __name__ == '__main__':
  display_dice()
  print(roll_dice(MIN_ROLL,MAX_ROLL))

