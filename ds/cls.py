#!/usr/bin/python3.6

# CLS.PY - Classifer
# let classifier read from a csv file?

import argparse
import pandas as pd
import matplotlib.pyplot as plt

class Cls:

    def __init__(self, csvfile, category, kvalue, dist_type='euclidean'):
        self.csvfile = csvfile       # csvfile to read from via pandas
        self.category = category     # Point category to classify
        self.kvalue = kvalue         # k nearest points
        self.dist_type = dist_type   # either Euclidean distance, or Hamming
        self._read()
        self._sort()

    def _read(self):
        self.df = pd.read_csv(self.csvfile)
        self.df.columns = ['Category','X','Y'] 
        self.df_cat_unique = self.df['Category'].unique()

        # Store data set in individual dataframe
        self.DATA = {}
        for i in range(len(self.df_cat_unique)):
             self.DATA[self.df_cat_unique[i]] = self.df[self.df['Category'] == self.df_cat_unique[i]]

    # TODO: Fails to work when ?-record is at the top of the data file
    def _sort(self):
        if self.dist_type == 'euclidean':
            self.df['D-Euclidean'] = ((self.df['X'] - self.DATA[self.category]['X'].values).pow(2) + (self.df['Y'] - self.DATA[self.category]['Y'].values).pow(2)).pow(0.5)
            self.df_sort = self.df.sort_values('D-Euclidean')
        elif self.dist_type == 'hamming':
            self.df['D-Hamming'] = (self.df['X'] - self.DATA[self.category]['X'].values).abs() + (self.df['Y'] - self.DATA[self.category]['Y'].values).abs()
            self.df_sort = self.df.sort_values('D-Hamming')
        self.df_result = self.df_sort.head(self.kvalue+1)  # returns confused point as well

    def GetPlot(self):
        for dkey in self.DATA.keys():
            plt.scatter(self.DATA[dkey]['X'], self.DATA[dkey]['Y'])
        plt.show()

    def GetResultSet(self):
        return self.df_result

    def GetDataSet(self):
        return self.df

    def GetCategory(self):
        self.cat_result = self.df_result['Category'].tail(self.kvalue).value_counts().idxmax()
        return self.cat_result

    def GetDistType(self):
        return self.dist_type

    def GetKValue(self):
        return self.kvalue

if __name__ == '__main__':

    # Create parent parser
    parser = argparse.ArgumentParser(description='Classifies orphan point by calculating k-nearest-neighbors.')

    # Create new argument group for compulsory arguments
    argsRequired = parser.add_argument_group('required named arguments')
    argsRequired.add_argument('-f', '--csvfile', required=True,
                              help='Reads dataset from CSV file.')
    argsRequired.add_argument('-c', '--category', required=True,
                              help='Data category of unclassified point.')
    argsRequired.add_argument('-k', '--kvalue', required=True,
                              help='Classify point according to K-nearest neighbors.')
    argsRequired.add_argument('-d', '--dist-type', required=True,
                              choices=['euclidean','hamming'],
                              help='Distance measuring algorithm.')

    # Initialize parser
    args = parser.parse_args()

    # Process input variables
    int_kvalue = int(args.kvalue)

    # Create classifier instance
    cls = Cls(csvfile=args.csvfile,
              category=args.category,
              kvalue=int_kvalue,
              dist_type=args.dist_type)

    print('Point classified as:', cls.GetCategory())
    print(cls.GetResultSet())
    cls.GetPlot()

