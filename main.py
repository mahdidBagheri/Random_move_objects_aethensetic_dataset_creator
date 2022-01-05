import os

import constants
from One_Batch import One_Batch
from Shapes import Shapes
from constants import *
import random

class Create_Dataset():
    def __init__(self):
        self.datasets_size = constants.datasets_size
        self.batch_size = constants.batch_size
        self.root_name = "./Data"

    def create(self):
        self.dataset_dir = self.find_dataset_dir()
        for i in range(self.datasets_size):
            print(f"creating batch{i}")
            # select shape
            shape = Shapes()
            one_batch = One_Batch(self.batch_size, shape, self.dataset_dir)
            one_batch.create()

    def create_root_directory(self):
        if(not os.path.isdir(self.root_name)):
            os.mkdir(self.root_name)

    def find_dataset_dir(self):
        self.create_root_directory()
        i = 0
        while(os.path.isdir(self.root_name + f"/dataset{i}")):
            i += 1
        os.mkdir(self.root_name + f"/dataset{i}")
        return self.root_name + f"/dataset{i}"

if __name__ == "__main__":
    data_set = Create_Dataset()
    data_set.create()
