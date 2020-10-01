import cv2 
import os 
from random_string import get_random_string


def _resize(ph_dir ,out_dir,scale_percent): 
    src = cv2.imread(f"{ph_dir}", cv2.IMREAD_UNCHANGED)
    width = int(src.shape[1] * scale_percent / 100)
    height = int(src.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(src, dsize)
    
    print(f"{out_dir}/{get_random_string(5)}.jpg")
    cv2.imwrite(f"{out_dir}/resized_{get_random_string(5)}.jpg", output)
     