#!/usr/bin/python3.6

# SORTS

import sys

class sort_class():

    def __init__(self, alist):
        self.tmplist = alist

    def _NewList(self, alist):
        if len(self.tmplist) > 0:
            self.tmplist = alist
        else:
            print('ERROR: List currently stored is already empty.')

    def _GetList(self):
        print('Original list:', self.tmplist) 

    def _InsertionSort(self):
        print(' *** INSERTION_SORT *** ')
        for i in reversed(range(1,len(self.tmplist))):
            for j in range(0,i):
                # print('i = %s, j = %s' %(i, j))
                if self.tmplist[j] > self.tmplist[j+1]:
                    key = self.tmplist.pop(j)
                    self.tmplist.insert(j+1, key)
                # print('Modified list =', self.tmplist)
            # print('Done with this inner loop.')
        return self.tmplist

    def _BubbleSort(self):
        pass

    def _MergeSort(self):
        pass

if __name__ == '__main__':
     list_A = [5,4,6,2,1,3]
     list_B = [22,91,2,64,87,31]
     x = sort_class(list_A)
     x._GetList()
     print(x._InsertionSort())
     x._NewList(list_B)
     x._GetList()
     print(x._InsertionSort())
