#!/usr/local/bin/python3
###############################
#   Bee-To-Home               #
#                             #
#   Benjamin Jakob, 11114701  #
#   Jon Follmann, 11099433    #
###############################

import matplotlib.pyplot as plt
import numpy as np
import vector
import snapshot
from sector import Sector


homePosition = np.array([0, 0])
home = plt.Circle(homePosition, 0.2, color='r')
lm1 = plt.Circle(np.array([3.5, 2]), 0.5)
lm2 = plt.Circle(np.array([3.5, -2]), 0.5)
lm3 = plt.Circle(np.array([0, -4]), 0.5)


# Neue Position einlesen
# x = float(input("Enter new x-position [Float]: "))
# y = float(input("Enter new y-position [Float]: "))
# newPosition = np.array([x, y])

# FOR TESTING: Fixed Position at (-3/-3)
newPosition = np.array([-3, -3])
homeSectors, homeGaps = snapshot.getSnapshot(homePosition)
newSectors, newGaps = snapshot.getSnapshot(newPosition)

rotationVector = snapshot.calculateRotation(homeSectors, homeGaps, newSectors, newGaps)
shiftVector = snapshot.calculateShift(homeSectors, homeGaps, newSectors, newGaps)
result = rotationVector + 3 * shiftVector

plt.figure()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bee to Home - Homevector')
plt.grid(True)
plt.axis([-8, 8, -8, 8])
plt.quiver(newPosition[0], newPosition[1], rotationVector[0], rotationVector[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(newPosition[0], newPosition[1], shiftVector[0], shiftVector[1], angles='xy', scale_units='xy', scale=1)
plt.quiver(newPosition[0], newPosition[1], result[0], result[1], angles='xy', scale_units='xy', color='r', scale=1)


fig, ax = plt.subplots()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bee to Home - Vectorfield')
plt.grid(True)
plt.axis([-8,8,-8,8])

for x in range(-7, 8):
    for y in range(-7, 8):
        if (x != 0 or y != 0) and (x != 0 or y != -4):
            newPosition = np.array([x, y])
            newSectors, newGaps = snapshot.getSnapshot(newPosition)
            rotationVector = snapshot.calculateRotation(homeSectors, homeGaps, newSectors, newGaps)
            shiftVector = snapshot.calculateShift(homeSectors, homeGaps, newSectors, newGaps)
            result = rotationVector + 3 * shiftVector
            plt.quiver(newPosition[0], newPosition[1], result[0], result[1], units='width')

ax.add_artist(home)
ax.add_artist(lm1)
ax.add_artist(lm2)
ax.add_artist(lm3)

plt.show()
