#!/usr/bin/python3.6

# SEQUENCE
# A very simple attempt at a sequence locking system
# Similar to the Oracle Sequence object, but with single data buffer

class Sequence():

    def __init__(self, 
                 startval, 
                 minval, 
                 maxval, 
                 stepval=1, 
                 seqlock=0, 
                 cycle=True, 
                 cache=1):
 
        self.minval = minval
        self.maxval = maxval
        self.stepval = stepval
        self.sequence = startval
        self.seqlock = seqlock   # No lock acquired upon creation, unless seqlock = 1
        self.cycle = cycle       # Cycle to minval upon reaching max
        self.cache = cache       # 0 = nocache, otherwise cache length
        self.maxflag = 0

        # Internal
        self.seqnextval = 0
        self.seqbuffer = 0       # Single value buffer for immediate next value
        self.cachebuffer = 0     # To populate cache entries
        self.cachecounter = 0    # Pointer to track cache entries
        self.SEQCACHE = []

        self.PopulateCache()
        print(self.SEQCACHE)

    def PopulateCache(self):

        if not self.cache:
            return 0

        if len(self.SEQCACHE) < self.cache:
            for i in range(self.cache - len(self.SEQCACHE)):
                self.SEQCACHE.append(self.NextSeq())

    def NextSeq(self):

        if self.seqbuffer + self.stepval > self.maxval:
            if self.cycle:
                self.seqbuffer = self.seqbuffer + self.stepval - self.maxval
        else:
            self.seqbuffer = self.seqbuffer + self.stepval

        return self.seqbuffer

    def GetNextSeq(self):

        if not self.AcquireLock():
            return 0

        # Return value from buffer
        if self.cache:
            self.seqnextval = self.SEQCACHE.pop(0)
            print('Current:', self.seqnextval)
            print('Next:', self.SEQCACHE[0])
            self.PopulateCache()
            print('SEQCACHE:', self.SEQCACHE)

        self.ReleaseLock()
        return self.seqnextval

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
    seq = Sequence(1,0,17,stepval=7, cache=7, cycle=True)

    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()

    seq.AcquireLock()

    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()
    seq.GetNextSeq()

    seq.ReleaseLock()

    seq.GetNextSeq()
