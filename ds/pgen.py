#!/usr/bin/python3.6

# PGEN.PY - Point generator

import csv
import random
import matplotlib.pyplot as plt

# Generate a random list of points stored as series of 3-tuples
# (category, x-coord, y-coord)
# Use PANDAS maybe?

class PointGen:

    def __init__(self,
                 category='A',
                 npoints=10,
                 min_x=0., min_y=0.,
                 max_x=1., max_y=1.):
        self.category = category
        self.npoints = npoints
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.POINTMAP = []
        self._Generate()

    def _Generate(self):
        for i in range(self.npoints):
            rand_x = random.uniform(self.min_x, self.max_x)
            rand_y = random.uniform(self.min_y, self.max_y)
            self.POINTMAP.append((self.category, rand_x, rand_y))
        self.pmap_x = [x[1] for x in self.POINTMAP]
        self.pmap_y = [x[2] for x in self.POINTMAP]

    def GetPoints(self):
        return self.POINTMAP

    def GetX(self):
        return self.pmap_x

    def GetY(self):
        return self.pmap_y


if __name__ == '__main__':

    A = PointGen(category='A', npoints=10, min_x=0.4, min_y=0.3, max_x=0.8, max_y=1.)
    map_A = A.GetPoints()
    x_A = A.GetX()
    y_A = A.GetY()

    B = PointGen(category='B', npoints=10, min_x=0.1, min_y=0.2, max_x=0.6, max_y=0.6)
    map_B = B.GetPoints()
    x_B = B.GetX()
    y_B = B.GetY()

    # Our confused point!
    P = PointGen(category='?', npoints=1, min_x=0.35, min_y=0.35, max_x=0.65, max_y=0.65)
    map_P = P.GetPoints()
    x_P = P.GetX()
    y_P = P.GetY()

    # Add all points to the CSV file
    with open('data.csv','w') as csvfile:
        cw = csv.writer(csvfile, delimiter=',')
        for s in map_A:
           cw.writerow(list(s))
        for s in map_B:
           cw.writerow(list(s))
        for s in map_P:
           cw.writerow(list(s))

    # Plot
    plt.scatter(x_A, y_A)
    plt.scatter(x_B, y_B)
    plt.scatter(x_P, y_P)
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

