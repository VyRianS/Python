#!/usr/bin/python3.6

# Runner class that runs to each closest point, exhausting a list of points

import math
import random

class MapGenerator():

    # Returns a list containing points around a 2-D map

    def __init__(self,
                 mapsize=(10.,10.),
                 npoints=10):
        # self.mapsize = mapsize
        self.max_x, self.max_y = mapsize
        self.npoints = npoints
        self.POINTMAP = []

    def RandomizePoints(self):
        for i in range(self.npoints):
            rand_x = random.uniform(0, self.max_x)
            rand_y = random.uniform(0, self.max_y)
            self.POINTMAP.append((rand_x, rand_y))

    def GetMap(self):
        self.RandomizePoints()
        return self.POINTMAP

class Runner():

    def __init__(self, 
                 run_list, 
                 start_position=(0.,0.), 
                 returnhome=False, 
                 show_stats=False):

        self.start_position = start_position
        self.position = start_position
        self.total_dist = 0
        self.dist_to_next = 0
        self.POINTS = run_list # pass in list of points
        self.VISITED = []
        self.RECORD = {}
        self.returnhome = returnhome
        self.show_stats = show_stats

    def MovePoint(self, point):
        self.dist_to_next = self.GetDist(point)
        # print('Moving %.2f units from %.2f to %.2f.' % (self.dist_to_next, self.position, point))
        print('Moving', self.dist_to_next, 'units, from', self.position, 'to', point) 
        self.position = point
        self.VISITED.append(point)
        self.total_dist += self.dist_to_next
        return self.position

    def NearestPoint(self):
        self.nearest = (math.inf, math.inf)
        for point, dist in self.RECORD.items():
            if dist < self.GetDist(self.nearest):
                self.nearest = point
        return self.nearest

    def GetDist(self, point):
        # method variables without self. prefix are not accessible to the instance?
        xloc, yloc = self.position
        dx, dy = point
        return math.sqrt((xloc - dx)**2 + (yloc - dy)**2)
        
    def StartRun(self):

        print('Starting run with the following map:')
        print(self.POINTS)
        
        while len(self.GetVisited()) < len(self.GetRunMap()):
            for point in self.POINTS:
                if point not in self.VISITED:
                    self.SetRecord(point, self.GetDist(point))
                else:
                    continue
            self.DisplayStatus()
            self.MovePoint(self.NearestPoint())
            self.RECORD.clear()

        if self.returnhome:
            print('Looping back to start position ...')
            self.MovePoint(self.start_position)
            self.RECORD.clear()
            self.DisplayStatus()

    def DisplayStatus(self):
        if self.show_stats:
            print('Current -', x.GetPosition())
            # print('VISITED -', x.GetVisited())
            # print('RECORD -', x.GetRecords())
            print('Total distance - {:.2f}'.format(self.total_dist))

    def SetRecord(self, point, dist):
        self.RECORD[point] = dist

    def GetPosition(self):
        return self.position

    def GetRecords(self):
        return self.RECORD

    def GetVisited(self):
        return self.VISITED
        
    def GetRunMap(self):
        return self.POINTS


#### END OF CLASS ####


if __name__ == '__main__':

    # Generate map
    runmap = MapGenerator(mapsize=(10.,10.), npoints=10)
    run_list = runmap.GetMap()

    # POINTS = [(4.,3.),(3.,2.),(1.,5.),(2.5,2.4),(6.,0.7)]
    x = Runner(start_position=(0.,0.), run_list=run_list, returnhome=True, show_stats=True)
    x.StartRun()

