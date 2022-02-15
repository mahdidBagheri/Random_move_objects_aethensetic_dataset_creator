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
        self.background_name = random.sample(glob.glob(constants.back_ground_address),1)[0]
        self.background = cv2.resize(cv2.imread(self.background_name),(640,480))
        self.size = int(random.random() * (constants.max_size - constants.min_size) + constants.min_size)
        self.icon_name = random.sample(glob.glob(constants.icons_address), 1)[0]
        icon = cv2.imread(self.icon_name)
        icon = cv2.resize(icon, (50, 50))
        self.icon = cv2.resize(icon, (self.size, self.size))
        self.icons = [Icons() for _ in range(constants.number_of_icons)]



class Icons():
    def __init__(self):

        y = random.randint(int(constants.Frame_Width / 10), int(9 * constants.Frame_Width / 10))
        x = random.randint(int(constants.Frame_Hight / 10), int(9 * constants.Frame_Hight / 10))
        [(x_, y_)] = random.sample(constants.dirs, 1)

        self.x = x
        self.y = y
        self.x_ = x_
        self.y_ = y_
