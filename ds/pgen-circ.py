#!/usr/bin/python3.6

# PGEN-RECT.PY - Point generator for rectangular boundaries

import argparse
import csv
import random
import math
import matplotlib.pyplot as plt

# Generate a random list of points stored as series of 3-tuples
# (category, x-coord, y-coord)

class PointGeneratorCirc:

    def __init__(self, category, npoints,
                 origin_x,
                 origin_y,
                 radius):
        self.category = category
        self.npoints = npoints
        self.or_x = origin_x
        self.or_y = origin_y
        self.radius = radius
        self.POINTS = []
        self._Generate()

    def _Generate(self):
        for i in range(self.npoints):
            # need to divide the upper radius bounds by 2, WHY???
            rand_r = random.uniform(0, self.radius/2)
            rand_a = random.uniform(0, math.pi*2)
            rand_x = self.or_x + rand_r**0.5 * math.cos(rand_a)
            rand_y = self.or_y + rand_r**0.5 * math.sin(rand_a)
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
    parser = argparse.ArgumentParser(description='Generate a series of N randomized 2-D points in a circular area given origin and maximum disk radius.')
    parser.add_argument('-p', '--plot', action='store_true',
                        help='Plots generated dataset.')
    parser.add_argument('-f', '--csvfile', help='Appends data into CSV file.')

    # Create new argument group for compulsory arguments
    argsRequired = parser.add_argument_group('required named arguments')
    argsRequired.add_argument('-c', '--category', required=True,
                              help='Data category, accepts any unique string.')
    argsRequired.add_argument('-n', '--nvalue', required=True,
                              help='Number of random points.')
    argsRequired.add_argument('-o', '--origin', required=True,
                              help='Coordinates in format: origin_x,origin_y.')
    argsRequired.add_argument('-r', '--radius', required=True,
                              help='Maximum radius of circle.')

    # Initialize parser
    args = parser.parse_args()

    # Process input variables
    int_nvalue = int(args.nvalue)
    flt_or_x = float(args.origin.split(',')[0])
    flt_or_y = float(args.origin.split(',')[1])
    flt_radius = float(args.radius)

    # Create point generator instance
    pgen = PointGeneratorCirc(category=args.category, 
                              npoints=int_nvalue, 
                              origin_x = flt_or_x,
                              origin_y = flt_or_y,
                              radius = flt_radius)

    # Add points a csv file
    if args.csvfile:
        with open(args.csvfile, 'a') as f:
            cw = csv.writer(f, delimiter=',')
            for coord in pgen.GetPoints():
                cw.writerow(list(coord))

    # Plot
    if args.plot:
        plt.scatter(pgen.GetX(),pgen.GetY())
        plt.grid(True)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

