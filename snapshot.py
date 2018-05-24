#!/usr/local/bin/python3

import numpy as np
import vector
from sector import Sector
import matplotlib.pyplot as plt

def getSnapshot(position):
    landmark_1  = np.array([3.5, 2]) - position
    landmark_2  = np.array([3.5, -2]) - position
    landmark_3  = np.array([0, -4]) - position

    sector_1 = getSector(landmark_1)
    sector_2 = getSector(landmark_2)
    sector_3 = getSector(landmark_3)

    sectorList = [sector_1, sector_2, sector_3]
    sectorList.sort(key=lambda x: vector.getRadian(x.getMiddle()))

    gapList = getGaps(sectorList)

    return sectorList, gapList


def getSector(landmark):
    tmp_n = vector.normalVector(landmark)
    n1 = vector.setLength(tmp_n, 0.5) * -1
    n2 = vector.setLength(tmp_n, 0.5)

    s1 = vector.unitVector(landmark + n1)
    s2 = vector.unitVector(landmark + n2)

    if vector.getRadian(s1) < vector.getRadian(s2):
        return Sector(s1, s2)
    else:
        return Sector(s2, s1)


def getGaps(sectorList):
    gapList = []

    for i in range(0,3):
        if vector.getRadian(sectorList[i].end) < vector.getRadian(sectorList[(i + 1) % 3].start):
            gapList.append(Sector(sectorList[i].end, sectorList[(i + 1) % 3].start))

    if len(gapList) == 0:
        minList = []
        maxList = []

        for i in range(0,3):
            if vector.getRadian(sectorList[i].start) < vector.getRadian(sectorList[i].end):
                minList.append(sectorList[i].start)
                maxList.append(sectorList[i].end)
            else:
                minList.append(sectorList[i].end)
                maxList.append(sectorList[i].start)

        minList.sort(key=lambda x: vector.getRadian(x))
        maxList.sort(key=lambda x: vector.getRadian(x))
        gapList.append(Sector(maxList[2], minList[0]))

    return gapList


def calculateRotation(homeSectors, homeGaps, currentSectors, currentGaps):
    rotationList = []
    rotation = np.array([0, 0])

    for s in homeSectors:
        closestSector = s.getClosest(currentSectors)
        rotationList.append(vector.unitVector(vector.normalVector(closestSector.getMiddle())))

    for s in homeGaps:
        closestSector = s.getClosest(currentGaps)
        rotationList.append(vector.unitVector(vector.normalVector(closestSector.getMiddle())))

    for v in rotationList:
        rotation = rotation + v

    return rotation


def calculateShift(homeSectors, homeGaps, currentSectors, currentGaps):
    shiftVectors = []
    shiftVector = np.array([0, 0])

    for s in homeSectors:
        closestSector = s.getClosest(currentSectors)
        if s.getRadian() > closestSector.getRadian():
            shiftVectors.append(vector.unitVector(closestSector.getMiddle()))
        else:
            shiftVectors.append(vector.unitVector(closestSector.getMiddle()) * -1)

    for s in homeGaps:
        closestSector = s.getClosest(currentGaps)
        if s.getRadian() > closestSector.getRadian():
            shiftVectors.append(vector.unitVector(closestSector.getMiddle()))
        else:
            shiftVectors.append(vector.unitVector(closestSector.getMiddle()) * -1)

    for v in shiftVectors:
        shiftVector = shiftVector + v

    return shiftVector
