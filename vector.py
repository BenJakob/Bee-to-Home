#!/usr/local/bin/python3
###############################
#   Bee-To-Home               #
#                             #
#   Benjamin Jakob, 11114701  #
#   Jon Follmann, 11099433    #
###############################

import numpy as np

def length( vector ):
   return np.linalg.norm(vector)

def normalVector( vector ):
    return np.array([vector[1] * -1, vector[0]])

def unitVector(vector):
    if np.linalg.norm(vector) != 0:
        return vector / np.linalg.norm(vector)
    else:
        return vector

def setLength( vector, newLength ):
    if np.linalg.norm(vector) != 0:
        return vector / np.linalg.norm(vector) * newLength
    else:
        return vector

def angleBetween(v1, v2):
    v1_u = unitVector(v1)
    v2_u = unitVector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def getRadian(vector):
    if getQuadrant(vector) == 1 or getQuadrant(vector) == 2:
        return angleBetween(np.array([1, 0]), vector)
    else:
        return angleBetween(np.array([-1, 0]), vector) + np.pi

def getQuadrant(vector):
    if vector[0] >= 0 and vector[1] >= 0:
        return 1
    elif vector[0] < 0 and vector[1] >= 0:
        return 2
    elif vector[0] < 0 and vector[1] < 0:
        return 3
    elif vector[0] >= 0 and vector[1] < 0:
        return 4
