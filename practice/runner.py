#!/usr/bin/python3.6

# Runner class that runs to each closest point, exhausting a list of points

import math

class Runner():

    def __init__(self, run_list, start_position=(0,0), returnhome=False):
        self.start_position = start_position
        self.position = start_position
        self.total_dist = 0
        self.POINTS = run_list # pass in list of points
        self.VISITED = []
        self.RECORD = {}
        self.returnhome = returnhome

    def MovePoint(self, point):
        self.dist_to_next = self.GetDist(point)
        print('Moving', self.dist_to_next, 'units from', self.position, 'to', point) 
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
        
        self.DisplayStatus()

        while len(self.GetVisited()) < len(self.GetRunMap()):
            print('*****')
            for point in self.POINTS:
                if point not in self.VISITED:
                    self.SetRecord(point, self.GetDist(point))
                else:
                    continue
            self.DisplayStatus()
            self.MovePoint(self.NearestPoint())
            self.RECORD.clear()
            self.DisplayDist()

        print('Looping back to start position ...')
        if self.returnhome:
            self.DisplayStatus()
            self.MovePoint(self.start_position)
            self.RECORD.clear()

        self.DisplayDist()

    def DisplayStatus(self):
        print('Current -', x.GetPosition())
        print('VISITED -', x.GetVisited())
        print('RECORD -', x.GetRecords())

    def DisplayDist(self):
        print('Total distance -', self.total_dist)

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

    POINTS = [(4.,3.),(3.,2.),(1.,5.),(2.5,2.4),(6.,0.7)]
    x = Runner(start_position=(-2,-3.4), run_list=POINTS, returnhome=True)
    x.StartRun()

