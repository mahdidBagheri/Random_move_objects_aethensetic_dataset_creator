Frame_Width = 640
Frame_Hight = 480
channels = 3
speed = 2
min_size = 40
max_size = 200
max_g_kernel = 5
datasets_size = 50
batch_size = 200
shapes = ["triangle", "rectangle", "circle" ]
precent_of_niosy_pixels = 0.02
back_ground_address = "./backgrounds/*.jpg"
icons_address = "./icons/*.png"
def get_frame_shape():
    return Frame_Hight, Frame_Width, 3