"""Description:
The script deals with the manupulation of images using the imaging library PIL. 
The images should be resized,and converted to .jpeg format.
The images are stored in a source directory and they should be saved in a manipulated state to an output directory.
This code is part 1 of the final grand assessment.
"""


#!/usr/bin/env python3

import os
from PIL import Image

src_dir = os.getcwd() + "\pictures" 
#The file path for the source directory, where the images are stored.
out_dir = os.getcwd() + "\modified_pictures" 

def convert_images(src_dir, out_dir):
    for filename in os.listdir(src_dir):
        src_path = src_dir + "/" + filename
        out_path = out_dir + "/" + filename[:-4] + "jpeg"
        if src_path[-4:] == "tiff":
            try:
                with Image.open(src_path) as im:
                    im = im.resize((600,400))
                    im = im.convert("RGB")
                    im.save(out_path,"JPEG")
                    im.close()
            except OSError:
                print("cannot convert", filename)

convert_images(src_dir=src_dir, out_dir=out_dir)
