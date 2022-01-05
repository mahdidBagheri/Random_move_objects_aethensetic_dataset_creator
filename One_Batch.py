import os.path
import random

import cv2
import math

import constants
from constants import *
import numpy as np


class One_Batch():
    def __init__(self, batch_size, shape, dataset_dir):
        self.batch_size = batch_size
        self.speed = constants.speed
        self.shape = shape
        self.dataset_dir = dataset_dir
        self.kernel_size = int(int(random.randint(1,int(constants.max_g_kernel/2)))*2+1)


    def find_batch_dir(self):
        i = 0
        while(os.path.isdir(self.dataset_dir + f"/batch{i}")):
            i += 1
        os.mkdir(self.dataset_dir + f"/batch{i}")
        return self.dataset_dir + f"/batch{i}"

    def create_frame(self, shape):
        back_ground = np.zeros(shape)
        return back_ground

    def create(self):
        self.batch_dir = self.find_batch_dir()

        dirs = [(-1*self.speed,-1*self.speed), (-1*self.speed,0), (0,-1*self.speed), (1*self.speed,1*self.speed), (1*self.speed,0), (0,1*self.speed)]
        x = random.randint(int(constants.Frame_Width/6),int(5*constants.Frame_Width/6))
        y = random.randint(int(constants.Frame_Hight/6),int(5*constants.Frame_Hight/6))
        [(x_, y_)] = random.sample(dirs, 1)

        for i in range(self.batch_size):
            change_dir = random.randint(0,50)
            if(change_dir >= 49):
                [(x_, y_)] = random.sample(dirs, 1)
                pass

            if(x + x_ > constants.Frame_Width ):
                x_ = -abs(x_)

            elif(x+x_ < 0):
                x_ = abs(x_)


            if(y + y_ > constants.Frame_Hight+40):
                y_ = -abs(y_)

            elif(y+y_ < 40):
                y_ = abs(y_)

            x = x + x_
            y = y + y_

            back_ground = self.create_frame(constants.get_frame_shape())
            if(self.shape.shape != "circle"):
                img = cv2.drawContours(back_ground,[self.shape.get_pts(x,y)], 0, self.shape.color  , -1)
            else:
                img = cv2.ellipse(back_ground, (int(x),int(y)),(self.shape.axis1 , self.shape.axis2), self.shape.angle, 0, 360, self.shape.color, -1)

            img = cv2.GaussianBlur(img,(self.kernel_size,self.kernel_size),0)
            img = self.add_noise(img)

            #cv2.imshow("image", img)
            #cv2.waitKey(50)

            img[:,:,:] *= 255
            cv2.imwrite(f"{self.batch_dir}/{i}.jpg", img)


    def add_noise(self, img):

        # Getting the dimensions of the image
        row, col, _ = img.shape

        # Randomly pick some pixels in the
        # image for coloring them white
        # Pick a random number between 300 and 10000
        number_of_pixels = int(480 * 640 * constants.precent_of_niosy_pixels/2)
        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to white
            img[y_coord][x_coord] = (255, 255, 255)

        # Randomly pick some pixels in
        # the image for coloring them black
        # Pick a random number between 300 and 10000
        number_of_pixels = int(480 * 640 * constants.precent_of_niosy_pixels/2)
        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to black
            img[y_coord][x_coord] = (0, 0, 0)

        return img