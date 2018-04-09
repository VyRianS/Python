#!/usr/bin/python3.6

# DICE ROLLER

import random

class DiceClass():

    def __init__(self):
        self.running = 1
        self.round_count = 0
        self.result_list = []
        self.default_min_roll = 1
        self.default_record_length = 10

    def PromptMinRoll(self):

        while True:
            self.min_roll = input('Lowest boundary: ')
            if not self.min_roll:
                self.min_roll = self.default_min_roll
                print('Default lowest boundary set to', self.default_min_roll)
                return self.min_roll

            # Ensure input is not a string
            try:
                int(self.min_roll)
            except ValueError:
                print('Invalid value, please re-input.')
                continue

            # Input is valid at this point
            return self.min_roll

    def PromptMaxRoll(self):

        while True:
            self.max_roll = input('Highest boundary: ')
            if not self.max_roll:
                self.max_roll = int(self.min_roll) + 1
                print('Default highest boundary set to', self.max_roll)
                return self.max_roll

            try:
                int(self.max_roll)
            except ValueError:
                print('Invalid value, please re-input.')
                continue

            if int(self.max_roll) <= int(self.min_roll):
                print('Highest bound must be at least 1 greater than minimum.')
                continue

            # Input is valid at this point
            return self.max_roll

    def PromptRecordLength(self):

        while True:
            self.record_length = input('Maximum records: ')
            if not self.record_length:
                self.record_length = self.default_record_length
                print('Maximum record length set to', self.default_record_length)
                return self.record_length

            try:
                int(self.record_length)
            except ValueError:
                print('Invalid value, please re-input.')
                continue

            if int(self.record_length) < 0: 
                print('Record must hold at least 1 historical result.')
                continue

            # Input is valid at this point
            return self.record_length
    
    def PromptContinue(self):

        while True:
            self.user_continue = input('Do you wish to continue? (Y/N) ')
            if not self.user_continue:
                self.running = 1
                return self.running
 
            if self.user_continue != 'Y' and self.user_continue != 'N':
                print('Invalid value, please re-input.')
                continue

            if self.user_continue == 'N':
                print('Thanks for playing!')
                self.running = 0
                return self.running

            # user_continue is 'Y'
            self.running = 1
            return self.running

    def DisplayState(self):
        print('Simulating a', self.max_roll, 'sided dice ...')
        print('MIN_ROLL =', self.min_roll, ' MAX_ROLL =', self.max_roll)

    def DisplayRecords(self):
        print(self.result_list)

    def DisplayAverage(self):
        print('Average of last', self.record_length, 'results:',sum(self.result_list)/float(len(self.result_list)))

    def ResetRound(self):
        self.round_count= 0
        self.result_list.clear()
        return self.round_count

    def RollDice(self):
        self.round_count += 1
        self.result = random.randint(int(self.min_roll), int(self.max_roll))
        print('Round', self.round_count, '- rolled', self.result)
        if len(self.result_list) == int(self.record_length):
            self.result_list.pop(0)
        self.result_list.append(self.result)
        return self.result

if __name__ == '__main__':

    # Instantiate dice object
    x = DiceClass()

    # User input for initial state
    x.PromptMinRoll()
    x.PromptMaxRoll()
    x.PromptRecordLength()
    x.DisplayState()

    # Game loop, x.running init with 1
    while x.running:
        x.RollDice()
        x.DisplayRecords()

        # Change flag x.running based on user input
        x.PromptContinue()
            
    print('Execution complete.')
