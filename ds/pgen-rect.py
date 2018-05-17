#!/usr/bin/python3.6

# PGEN-RECT.PY - Point generator for rectangular boundaries

import argparse
import csv
import random
import matplotlib.pyplot as plt

# Generate a random list of points stored as series of 3-tuples
# (category, x-coord, y-coord)

class PointGeneratorRect:

    def __init__(self, category, npoints,
                 min_x, min_y,
                 max_x, max_y):
        self.category = category
        self.npoints = npoints
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.POINTS = []
        self._Generate()

    def _Generate(self):
        for i in range(self.npoints):
            rand_x = random.uniform(self.min_x, self.max_x)
            rand_y = random.uniform(self.min_y, self.max_y)
            self.POINTS.append((self.category, rand_x, rand_y))
        self.POINTS_X = [x[1] for x in self.POINTS]
        self.POINTS_Y = [x[2] for x in self.POINTS]

    def GetPoints(self):
        return self.POINTS

    def GetX(self):
        return self.POINTS_X

    def GetY(self):
        return self.POINTS_Y


if __name__ == '__main__':

    # Create parent parser
    parser = argparse.ArgumentParser(description='Generate a series of N randomized 2-D points in a rectangular area within minimum and maximum boundaries.')
    parser.add_argument('-p', '--preview-bounds', action='store_true',
                        help='Displays area bounded by upper and lower coordinates.')
    parser.add_argument('-f', '--csvfile', help='Appends data into CSV file.')

    # Create new argument group for compulsory arguments
    argsRequired = parser.add_argument_group('required named arguments')
    argsRequired.add_argument('-c', '--category', required=True,
                              help='Data category, accepts any unique string.')
    argsRequired.add_argument('-n', '--nvalue', required=True,
                              help='Number of random points.')
    argsRequired.add_argument('-x', '--xbounds', required=True,
                              help='Coordinates in format: min_x,max_x.')
    argsRequired.add_argument('-y', '--ybounds', required=True,
                              help='Coordinates in format: min_y,max_y.')

    # Initialize parser
    args = parser.parse_args()

    # Process input variables
    int_nvalue = int(args.nvalue)
    flt_min_x = float(args.xbounds.split(',')[0])
    flt_max_x = float(args.xbounds.split(',')[1])
    flt_min_y = float(args.ybounds.split(',')[0])
    flt_max_y = float(args.ybounds.split(',')[1])

    # Create point generator class
    pgen = PointGeneratorRect(category=args.category, 
                              npoints=int_nvalue, 
                              min_x=flt_min_x, 
                              min_y=flt_min_y, 
                              max_x=flt_max_x, 
                              max_y=flt_max_y)

    # Add points a csv file
    if args.csvfile:
        with open(args.csvfile, 'a') as f:
            cw = csv.writer(f, delimiter=',')
            for coord in pgen.GetPoints():
                cw.writerow(list(coord))

    # Display preview
    if args.preview_bounds:
        plt.axhspan(ymin=flt_min_y,
                    ymax=flt_max_y,
                    xmin=flt_min_x,
                    xmax=flt_max_x,
                    color='r',
                    fill=False)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

    '''
    # Plot
    plt.scatter(x_A, y_A)
    plt.scatter(x_B, y_B)
    plt.scatter(x_P, y_P)
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    '''
