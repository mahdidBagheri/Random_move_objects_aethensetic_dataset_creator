import colorsys
import glob
import math
import random

import cv2
import numpy as np
import constants

"""
class Shapes():
    def __init__(self):
        self.shape = random.sample(constants.shapes,1)[0]
        self.size = random.randint(constants.min_size, constants.max_size)
        self.color = colorsys.hsv_to_rgb(random.random(), random.random(), (random.random()+1)/2)
        self.e1 = random.randint(1,int(self.size/4))
        self.e2 = random.randint(1,int(self.size/4))
        self.axis1 = random.randint(1, int(self.size/2))
        self.axis2 = random.randint(1, int(self.size/2))
        self.angle = random.randint(0,359)

    def get_pts(self, x, y):
        if(self.shape == "triangle"):
            pts1 = (int(x), int(y - math.floor(math.sqrt(3) / 2 * self.size)))
            pts2 = (int(x - math.floor(self.size / 3)), int(y - math.floor(self.size / 2)))
            pts3 = (int(x + math.floor(self.size / 3)), int(y - math.floor(self.size / 2)))
            return np.array([pts1, pts2, pts3])

        elif(self.shape == "rectangle"):
            pts1 = (int(x - self.size/2 + self.e1),int(y - self.size/2 + self.e2 ))
            pts2 = (int(x + self.size/2 - self.e1),int(y - self.size/2 + self.e2))
            pts3 = (int(x + self.size/2 - self.e1),int(y + self.size/2 - self.e2))
            pts4 = (int(x - self.size/2 + self.e1),int(y + self.size/2 - self.e2))
            return np.array([pts1, pts2, pts3,pts4])

        elif(self.shape == "circle"):
            pass
"""

class Shapes():
    def __init__(self):

        self.background = cv2.resize(cv2.imread(random.sample(glob.glob(constants.back_ground_address),1)[0]),(640,480))
        self.size = (random.random() + 0.1) * 2

        icon = cv2.imread(random.sample(glob.glob(constants.icons_address),1)[0])
        icon = cv2.resize(icon,(50,50))
        self.icon = cv2.resize(icon, (int(icon.shape[0]*self.size), int(icon.shape[1]*self.size)))



