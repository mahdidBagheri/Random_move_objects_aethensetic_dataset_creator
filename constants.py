Frame_Width = 640
Frame_Hight = 480
channels = 3
speed = 2
min_size = 75
max_size = 150
max_g_kernel = 5
datasets_size = 5
batch_size = 100
dirs = [(-1 * speed, -1 * speed), (-1 * speed, 0), (0, -1 * speed),
        (1 * speed, 1 * speed), (1 * speed, 0), (0, 1 * speed)]
number_of_icons = 15
shapes = ["triangle", "rectangle", "circle" ]
precent_of_niosy_pixels = 0.02
back_ground_address = "./backgrounds/*.jpg"
icons_address = "./icons/*.png"
def get_frame_shape():
    return Frame_Hight, Frame_Width, 3