#!/usr/bin/python3.6

# SORTS
# Python implementation of several sort algorithms

class sort_class():

    def __init__(self, alist):
        self.tmplist = alist
        self._RaiseEmptyList()

    def _RaiseEmptyList(self):
        if len(self.tmplist) == 0:
            print('WARNING: List currently stored is empty.')

    # Same as __init__(self), condense?
    def _NewList(self, alist):
        self.tmplist = alist
        self._RaiseEmptyList()

    def _GetList(self):
        print('Original list:', self.tmplist) 

    def _InsertionSort(self):
        print(' *** INSERTION_SORT *** ')
        for i in reversed(range(1,len(self.tmplist))):
            for j in range(0,i):
                if self.tmplist[j] > self.tmplist[j+1]:
                    key = self.tmplist.pop(j)
                    self.tmplist.insert(j+1, key)
        return self.tmplist

    def _BubbleSort(self):
        pass

    def _MergeSort(self):
        pass

if __name__ == '__main__':
     """
     list_A = [5,4,6,2,1,3]
     list_B = [22,91,2,64,87,31]
     x = sort_class(list_A)
     x._GetList()
     print(x._InsertionSort())
     x._NewList(list_B)
     x._GetList()
     print(x._InsertionSort())
     """

     list_E = []
     x = sort_class(list_E)
