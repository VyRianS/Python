#!/usr/bin/python3.6

# CLS.PY - Classifer
# let classifier read from a csv file?

import pandas as pd
import matplotlib.pyplot as plt

class Classifier:

    def __init__(self, csvfile, kvalue, dist_type='euclidean'):
        self.csvfile = csvfile       # csvfile to read from via pandas
        self.kvalue = kvalue        # k nearest points
        self.dist_type = dist_type   # either Euclidean distance, or Hamming
        self._read()
        self._sort()

    def _read(self):
        self.df = pd.read_csv(self.csvfile)
        self.df.columns = ['Class','X','Y'] 
        self.df_p = self.df[self.df['Class'] == '?']

    def _sort(self):
        if self.dist_type == 'euclidean':
            self.df['D-Euclidean'] = ((self.df['X']-self.df_p['X'].values).pow(2) + (self.df['Y']-self.df_p['Y'].values).pow(2)).pow(0.5)
            self.df_sort = self.df.sort_values('D-Euclidean')
        elif self.dist_type == 'hamming':
            self.df['D-Hamming'] = (self.df['X']-self.df_p['X'].values).abs() + (self.df['Y']-self.df_p['Y'].values).abs()
            self.df_sort = self.df.sort_values('D-Hamming')
        self.df_result = self.df_sort.head(self.kvalue+1)

    def GetResultSet(self):
        return self.df_result

    def GetDataSet(self):
        return self.df

    def GetClass(self):
        self.class_result = self.df_result['Class'].tail(self.kvalue).value_counts().idxmax()
        return self.class_result

    def GetDistType(self):
        return self.dist_type

    def GetKValue(self):
        return self.kvalue

if __name__ == '__main__':

    cls = Classifier(csvfile='testdata.csv', kvalue=10, dist_type='euclidean')
    print('?-point classified as:', cls.GetClass())
    print(cls.GetResultSet())

    '''
    # Visualize
    plt.scatter(df_A['X'], df_A['Y'])
    plt.scatter(df_B['X'], df_B['Y'])
    plt.scatter(df_P['X'], df_P['Y'])
    plt.show()
    '''
