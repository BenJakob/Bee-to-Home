#!/usr/local/bin/python3
###############################
#   Bee-To-Home               #
#                             #
#   Benjamin Jakob, 11114701  #
#   Jon Follmann, 11099433    #
###############################

import numpy as np
import vector
from sector import Sector
import matplotlib.pyplot as plt

def getSnapshot(position):

    # Definition von Landmarks
    landmark_1  = np.array([3.5, 2]) - position
    landmark_2  = np.array([3.5, -2]) - position
    landmark_3  = np.array([0, -4]) - position

    # Normalvektor von den Landmarks berechnen
    tmp_n = vector.normalVector(landmark_1)
    landmark_1_n1 = vector.setLength(tmp_n, 0.5) * -1
    landmark_1_n2 = vector.setLength(tmp_n, 0.5)

    tmp_n = vector.normalVector(landmark_2)
    landmark_2_n1 = vector.setLength(tmp_n, 0.5) * -1
    landmark_2_n2 = vector.setLength(tmp_n, 0.5)

    tmp_n = vector.normalVector(landmark_3)
    landmark_3_n1 = vector.setLength(tmp_n, 0.5) * -1
    landmark_3_n2 = vector.setLength(tmp_n, 0.5)

    # Schnittpunkte auf der Snapshot-Retina bestimmen
    landmark_1_s1 = vector.unitVector(landmark_1 + landmark_1_n1)
    landmark_1_s2 = vector.unitVector(landmark_1 + landmark_1_n2)

    landmark_2_s1 = vector.unitVector(landmark_2 + landmark_2_n1)
    landmark_2_s2 = vector.unitVector(landmark_2 + landmark_2_n2)

    landmark_3_s1 = vector.unitVector(landmark_3 + landmark_3_n1)
    landmark_3_s2 = vector.unitVector(landmark_3 + landmark_3_n2)

    # Sektoren
    sector_1 = Sector(landmark_1_s1, landmark_1_s2)
    sector_2 = Sector(landmark_2_s1, landmark_2_s2)
    sector_3 = Sector(landmark_3_s1, landmark_3_s2)

    sectorList = [sector_1, sector_2, sector_3]
    sectorList.sort(key=lambda x: vector.getRadian(x.getMiddle()))

    gapList = getGaps(sectorList)
    gapList.sort(key=lambda x: vector.getRadian(x.getMiddle()))

    return sectorList, gapList

def getGaps(sectorList):
    gapList = []
    minList = []
    maxList = []

    for i in range(0,3):
        if vector.getRadian(sectorList[i].start) < vector.getRadian(sectorList[i].end):
            minList.append(sectorList[i].start)
            maxList.append(sectorList[i].end)
        else:
            minList.append(sectorList[i].end)
            maxList.append(sectorList[i].start)

    for i in range(0,2):
        if vector.getRadian(sectorList[i].end) < vector.getRadian(sectorList[i + 1].start):
            gapList.append(Sector(sectorList[i].end, sectorList[i + 1].start))

    if len(gapList) == 0:
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
