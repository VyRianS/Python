#!/usr/bin/python3.6

# Simple simulation of data structures within memory using python

# Memory is a static length list of 100 addresses
# Memory addresses are the list indexes
# Empty data is 'None'
MEMORY = [None for x in range(100)]

# Currently using too many Python-specific functions
# Try to do everything using the pointer to simulate lower-level behavior

class ArrayClass():

    def __init__(self, head, length):
        self.head = head
        self.tail = head + length - 1   # due to 0-indexing
        self.length = length
        self.pointer = self.head        # Point to the first empty address
        self.emptyflag = None

    def _ResetPtr(self):
        self.pointer = self.head
        return self.pointer

    def _MovePtr(self, new_pos):
        self.pointer += new_pos
        return self.pointer

    def _GetPtrPos(self):
        return self.pointer

    def ArrayDelete(self, index):
        address_delete = self.head + index

        if address_delete > self.tail:
            print('SEGFAULT - Array delete out of bounds!')
            return 1

        if MEMORY[address_delete] == self.emptyflag:
            print('ERROR - Value at index', index, 'is already empty!')
            return 1

        # constant time movement of pointer
        self._MovePtr(index)
        MEMORY[self.pointer] = self.emptyflag
        self._ResetPtr()
        return 0

    def ArrayInsert(self, index, value):
        address_insert = self.head + index

        if address_insert > self.tail:
            print('SEGFAULT - Array insert out of bounds!')
            return 1

        if MEMORY[address_insert] != self.emptyflag:
            print('SEGFAULT - Index at', index, 'is already filled!')
            return 1

        self._MovePtr(index)
        MEMORY[self.pointer] = value
        self._ResetPtr()
        return 0

    def GetArray(self):
        return MEMORY[self.head:self.tail+1]

if __name__ == '__main__':
    
    a = ArrayClass(head=0, length=5)
    a.ArrayInsert(0,'pos0')
    a.ArrayInsert(4,'pos4')
    a.ArrayInsert(5,'segfault')
    a.ArrayInsert(2,'data00')
    a.ArrayDelete(2)
    print(a.GetArray())

    b = ArrayClass(head=94, length=4)
    b.ArrayInsert(0,'pos0')
    b.ArrayInsert(3,'NA')
    print(b.GetArray())

    #print('MEMORY length:', len(MEMORY))
    #print('First 10:', MEMORY[:10])
    #print('Last 10:', MEMORY[-10:]) 

