#!/usr/local/bin/python3

import numpy as np

def length(vector):
   return np.linalg.norm(vector)

def normalVector(vector):
    return np.array([vector[1] * -1, vector[0]])

def unitVector(vector):
    if np.linalg.norm(vector) != 0:
        return vector / np.linalg.norm(vector)
    else:
        return vector

def setLength(vector, newLength):
    if np.linalg.norm(vector) != 0:
        return vector / np.linalg.norm(vector) * newLength
    else:
        return vector

def angleBetween(v1, v2):
    return np.arccos(np.clip(np.dot(unitVector(v1), unitVector(v2)), -1.0, 1.0))

def getRadian(vector):
    return np.arctan2(vector[1], vector[0])
