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
                 cache=5):
 
        self.minval = minval
        self.maxval = maxval
        self.stepval = stepval
        self.sequence = startval
        self.seqlock = seqlock   # No lock acquired upon creation
        self.cycle = cycle       # Cycle to minval upon reaching max
        self.cache = cache       # 0 = nocache, otherwise cache length
        self.maxflag = 0

        # Internal
        self.seqbuffer = 0       # Buffer to insert into cache
        self.SEQCACHE = []

    def NextSeq(self):

        if self.sequence + self.stepval > self.maxval:
            if self.cycle:
                self.seqbuffer = self.sequence + self.stepval - self.maxval
            else:
                self.maxflag = 1
        else:
            self.seqbuffer = self.sequence + self.stepval

        return self.seqbuffer

    def IncreaseSeq(self):

        if not self.AcquireLock():
            return 0

        # Return value from buffer
        self.sequence = self.NextSeq()

        if self.maxflag:
            print('Unable to increase, sequence would exceed maximum!')

        print('Current:', self.sequence)
        print('Next:', self.NextSeq())
        self.ReleaseLock()
        return 1

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
    seq = Sequence(1,0,63,stepval=7,cycle=True)

    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()

    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
    seq.IncreaseSeq()
