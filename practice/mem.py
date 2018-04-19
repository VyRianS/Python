#!/usr/bin/python3.6

# MEM.py - Simulation of simple memory structure

class MemoryBuffer:

    def __init__(self, bufsize):
        self.bufsize = bufsize
        self.bufhead = 0
        self.buftail = bufsize - 1
        self.emptyflag = None
        self.BUFFER = [self.emptyflag for x in range(self.bufsize)]
        self.OBJLOOKUP = {}
        self.ptr = 0         # Main pointer for class
        self.ptr_hwm = 0     # Pointer to high-water-mark in buffer
        self.allowed_types = ('S_Array','D_Array')

    def GetBuf(self):
        return self.BUFFER

    def GetLookup(self):
        return self.OBJLOOKUP

    # Pointer functionality for future updates
    def _ResetPtr(self):
        self.ptr = 0
        return self.ptr

    def _MovePtr(self, pos):
        self.ptr += pos
        return self.ptr

    def _GetPtr(self):
        return self.ptr
    ##############################

    def FlushBuf(self):
        for i in range(len(self.BUFFER)):
            if self.BUFFER[i] != self.emptyflag:
                self.BUFFER[i] = self.emptyflag
        self.OBJLOOKUP.clear()
        return 0

    def AllocBuf(self, name, objtype, head, length):
        if objtype not in self.allowed_types:
            print('AllocBuf - Unknown object type!')
            return 1

        if head + length - 1 > len(self.BUFFER):
            print('AllocBuf - Out of allocated memory bounds!')
            return 1

        self.OBJLOOKUP[name] = (objtype, head, head+length-1)
        return head          # Returns value at the first element of object

    def FreeBuf(self, name, defrag=False):
        # Deletes object and frees buffer
        if name not in self.OBJLOOKUP.keys():
            print('FreeBuf - Object does not exist in lookup!')
            return 1
        head = self.GetObjBounds(name)[1]
        tail = self.GetObjBounds(name)[2]
        for i in range(head, tail+1):
            self.BUFFER[i] = self.emptyflag
        del self.OBJLOOKUP[name]
        return 0 # Return something else?

    def GetObjBounds(self, name):
        # Returns object type, head, and tail addresses as a list
        if name not in self.OBJLOOKUP.keys():
            print('GetObjBounds - Object does not exist in lookup!')
            return 1
        return list(self.OBJLOOKUP[name])

    def SetValue(self, name, pos, value):
        # Sets value in memory, assuming it is already allocated
        # head is position 0, tail is position (length-1)
        if name not in self.OBJLOOKUP.keys():
            print('SetValue - Object does not exist in lookup!')
            return 1
        head = self.GetObjBounds(name)[1]
        tail = self.GetObjBounds(name)[2]
        if pos < 0 or (pos + head) > tail:
            print('SetValue - Invalid relative object index!')
            return 1
        self.BUFFER[head+pos] = value
        return 0 

    def GetObj(self, name):
        if name not in self.OBJLOOKUP.keys():
            print('GetObj - Object does not exist in lookup!')
            return 1
        head = self.GetObjBounds(name)[1]
        tail = self.GetObjBounds(name)[2]
        return self.BUFFER[head:tail+1]

if __name__ == '__main__':
    x = MemoryBuffer(bufsize=12)
    print(x.AllocBuf(name='dunes', objtype='S_Array', head=1, length=4))
    x.AllocBuf(name='list', objtype='S_Array', head=7, length=3)
    x.SetValue('dunes', 2, '@!#%') 
    x.SetValue('list', 2, '&&&&&')
    print(x.GetBuf())
    print(x.GetLookup())
    print(x.GetObj('dunes'))
    print(x.GetObj('list'))

    x.FreeBuf(name='dunes')
    print(x.GetBuf())
    print(x.GetLookup())
   
    x.FlushBuf()
    print(x.GetBuf())
    print(x.GetLookup())
