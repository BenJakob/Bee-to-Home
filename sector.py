#!/usr/local/bin/python3

import numpy as np
import vector

class Sector:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getMiddle(self):
        if vector.getRadian(self.end) - vector.getRadian(self.start) > np.pi:
            return vector.unitVector(self.start + self.end) * -1
        else:
            return vector.unitVector(self.start + self.end)

    def getRadian(self):
        return vector.getRadian(self.end) - vector.getRadian(self.start)

    def getClosest(self, sectorList):
        minDistance = vector.length(self.getMiddle() - sectorList[0].getMiddle())
        closestSector = sectorList[0]

        for s in sectorList:
            if vector.length(self.getMiddle() - s.getMiddle()) < minDistance:
                minDistance = vector.length(self.getMiddle() - s.getMiddle())
                closestSector = s

        return closestSector
