#!/usr/bin/python3.6

# SEQUENCE
# A very simple attempt at a sequence locking system
# Similar to the Oracle Sequence object

class Sequence():

    def __init__(self, 
                 startval, 
                 minval, 
                 maxval, 
                 stepval=1, 
                 seqlock=0, 
                 cycle=True, 
                 cache=1):
 
        # Constructors
        self.sequence = startval   # Current sequence value
        self.minval = minval       # Minimum boundary
        self.maxval = maxval       # Maximum boundary
        self.stepval = stepval     # Increment per step
        self.seqlock = seqlock     # No lock acquired upon creation, unless seqlock = 1
        self.cycle = cycle         # Cycle to minval upon reaching max
        self.cache = cache         # 0 = nocache, otherwise cache length
        self.c = None              # Iterative counter

        # Internal
        self.seqbuffer = startval  # Single value buffer for immediate next value
        self.SEQCACHE = []

        # Initialization methods
        self.PopulateCache()       # Populate cache entries

        if not all(isinstance(self.c, int) for self.c in [startval, minval, maxval, stepval, cache]):
            # TODO: returns value instead of constructor
            raise ValueError('Constructor', self.c, 'is not of type INT!') 

    def GenerateNextSeq(self):
        if self.seqbuffer + self.stepval > self.maxval:
            if self.cycle:
                self.seqbuffer = self.seqbuffer + self.stepval - self.maxval
        else:
            self.seqbuffer = self.seqbuffer + self.stepval
        return self.seqbuffer

    def PopulateCache(self):
        for i in range(self.cache - len(self.SEQCACHE)):
            self.SEQCACHE.append(self.GenerateNextSeq())

    def GetCurrentSeq(self):
        return self.sequence

    def GetCache(self):
        return self.SEQCACHE

    def GetNextSeq(self):
        if not self.AcquireLock():
            return 0
        # Return value from buffer
        if self.cache:
            self.sequence = self.SEQCACHE.pop(0)
            self.PopulateCache()
        else:
            self.sequence = self.GenerateNextSeq()
        print('Current:', self.sequence)
        self.ReleaseLock()
        return self.sequence

    def AcquireLock(self):
        if not self.seqlock:
            self.seqlock = 1
            return 1
        else:
            print('Unable to obtain lock.')
            return 0

    def ReleaseLock(self):
        if self.seqlock:
            self.seqlock = 0
            return 1
        else:
            print('Sequence is not locked.')
            return 0

if __name__ == '__main__':

    testseq = Sequence(startval=8, minval='asd', maxval=23)

    seq = Sequence(startval=1, minval=0, maxval=23, stepval=7, cache=3, cycle=True)

    print(seq.GetCurrentSeq())
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()

    seq.AcquireLock()

    seq.GetNextSeq()
    seq.GetNextSeq()

    seq.ReleaseLock()

    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
