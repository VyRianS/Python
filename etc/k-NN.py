#!/usr/bin/python3.6

# K-NN.py - K-Nearest Neighbors

import random
import matplotlib.pyplot as plt

# Map generator class
class MapGenerator:

    def __init__(self, 
                 size=(10.,10.), 
                 npoints=50):
        self.size = size          # Map size
        self.npoints = npoints    # Number of points
        self.POINTMAP = []        # List of points
        self.MAP_X = []
        self.MAP_Y = []
        self.RandomizePoints()

    def RandomizePoints(self):
        max_x, max_y = self.size
        for i in range(self.npoints):
            rand_x = random.uniform(0, max_x)
            rand_y = random.uniform(0, max_y)
            self.MAP_X.append(rand_x)
            self.MAP_Y.append(rand_y)
            self.POINTMAP.append((rand_x, rand_y))

    def GetMap(self):
        return self.POINTMAP

    def GetPoints_X(self):
        return self.MAP_X

    def GetPoints_Y(self):
        return self.MAP_Y

if __name__ == '__main__':
    map = MapGenerator()
    print(map.GetMap())

    t = map.GetPoints_X()
    s = map.GetPoints_Y()
    plt.scatter(t,s)

    plt.grid(True)
    plt.title('Test')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
