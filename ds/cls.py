#!/usr/bin/python3.6

# CLS.PY - Classifer
# let classifier read from a csv file?

import pandas as pd
import matplotlib.pyplot as plt

class Classifier:

    def __init__(self, csvfile, kpoints, dist_type='euclidean'):
        self.csvfile = csvfile       # csvfile to read from via pandas
        self.kpoints = kpoints       # k nearest points
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
        self.df_result = self.df_sort['Class'].head(self.kpoints+1).tail(self.kpoints)

    def GetResultSet(self):
        return self.df_result

    def GetDataSet(self):
        return self.df

    def GetClass(self):
        self.class_result = self.df_result.value_counts().idxmax()
        return self.class_result

if __name__ == '__main__':

    cls = Classifier(csvfile='data.csv', kpoints=5, dist_type='hamming')
    print(cls.GetClass())
    print(cls.GetResultSet())

    '''
    df = pd.read_csv('data.csv')
    df.columns = ['Class','X','Y']

    # Filter dataframe based off Class
    df_A = df[df['Class'] == 'A']
    df_B = df[df['Class'] == 'B']

    # Our confused point
    df_P = df[df['Class'] == '?']

    # Euclidean distance from ?-point
    df['D-Euclidean'] = ((df['X']-df_P['X'].values).pow(2) + (df['Y']-df_P['Y'].values).pow(2)).pow(0.5)

    # Hamming distance
    df['D-Hamming'] = (df['X']-df_P['X'].values).abs() + (df['Y']-df_P['Y'].values).abs()
    print(df)

    # Sort based on Euclidean distance
    df_sort = df.sort_values('D-Euclidean')

    # Find classification result
    class_result = df_sort['Class'].head(6).tail(5).value_counts().idxmax()
    print(class_result)
    # Visualize
    plt.scatter(df_A['X'], df_A['Y'])
    plt.scatter(df_B['X'], df_B['Y'])
    plt.scatter(df_P['X'], df_P['Y'])
    plt.show()
    '''
