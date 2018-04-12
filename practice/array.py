#!/usr/bin/python3.6

# Simple simulation of data structures within memory using python

# Memory is a static length list of 100 addresses
# Memory addresses are the list indexes
# Empty data is -1
MEMORY = [-1 for x in range(100)]

# Currently using too many Python-specific functions
# Try to do everything using the pointer to simulate lower-level behavior

class ArrayClass():

    def __init__(self, address_head, length):
        self.address_head = address_head
        self.address_tail = address_head + length + 1
        self.length = length
        self.pointer = self.address_head + 1 # Point to the first empty address
        self.emptyflag = -1

        # Insert array's head and tail markers
        # Data can only be inserted between these markers
        self.headmarker = self.address_head + 1
        self.tailmarker = self.address_tail

        MEMORY.pop(self.address_head)
        MEMORY.insert(self.address_head, 'HEAD:'+str(self.address_head))
        MEMORY.pop(self.address_tail)
        MEMORY.insert(self.address_tail, 'TAIL:'+str(self.address_tail))

    def _ResetPtr(self):
        self.pointer = self.address_head + 1
        return self.pointer

    def _MovePtr(self, new_pos):
        self.pointer += new_pos
        return self.pointer

    def _GetPtrPos(self):
        return self.pointer

    def ArrayInsert(self, index, value):
        # Check if index is out of bounds
        address_insert = self.address_head + index + 1

        if address_insert > self.address_tail:
            print('SEGFAULT - Array insert out of bounds!')
            return 1

        if MEMORY[address_insert] != -1:
            print('SEGFAULT - Index at', index, 'is already filled!')
            return 1

        # Pointer movement is constant time due to addition of addresses
        self.pointer += index              # 0-indexed
        MEMORY.pop(self.pointer)
        MEMORY.insert(self.pointer, value)

        # Reset pointer
        self._ResetPtr()
        return 0

    def GetArray(self):
        return MEMORY[self.headmarker:self.tailmarker]

if __name__ == '__main__':
    
    a = ArrayClass(address_head=0, length=5)
    a.ArrayInsert(0,'pos0')
    a.ArrayInsert(4,'pos4')
    print(a.GetArray())

    b = ArrayClass(address_head=94, length=4)
    b.ArrayInsert(0,'pos0')
    b.ArrayInsert(3,'NA')
    print(b.GetArray())

    print('MEMORY length:', len(MEMORY))
    print('First 10:', MEMORY[:10])
    print('Last 10:', MEMORY[-10:]) 

