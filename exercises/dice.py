#!/usr/bin/python3.6

# DICE ROLLER

import random

class DiceClass():

    def __init__(self):
        self.round_count = 0
        self.result_list = []

    def _SetState(self):

        # Min roll, negative values are OK
        self.min_roll = input('Lowest boundary: [1] ') or 1

        # Check that max_roll is greater than min_roll
        while True:
            self.max_roll = input('Highest boundary: [6] ') or 6
            if int(self.max_roll) <= int(self.min_roll):
                print('Invalid value, too low.')
            else:
                break

        # Check that length is not negative
        while True:
            self.max_record_length = input('Number of rolls to record: [10] ') or 10
            if int(self.max_record_length) <= 0:
                print('At least 1 record must be kept.')
            else:
                break

    def _DisplayState(self):
        print('Simulating a', self.max_roll, 'sided dice ...')
        print('MIN_ROLL =', self.min_roll, ' MAX_ROLL =', self.max_roll)

    def _DisplayRecords(self):
        print(self.result_list)

    def _DisplayAverage(self):
        print('Last 10 average:',sum(self.result_list)/float(len(self.result_list)))

    def _ResetRound(self):
        self.round_count= 0
        self.result_list.clear()
        return self.round_count

    def _RollDice(self):
        self.round_count += 1
        self.result = random.randint(int(self.min_roll), int(self.max_roll))
        print('Round', self.round_count, '- rolled', self.result)
        if len(self.result_list) == int(self.max_record_length):
            self.result_list.pop(0)  # Remove first item from list
        self.result_list.append(self.result)
        return self.result

if __name__ == '__main__':

    # Instantiate dice object
    x = DiceClass()

    # User input for initial state
    x._SetState()
    x._DisplayState()

    # Game loop
    while True:
        x._RollDice()
        x._DisplayRecords()
        
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
