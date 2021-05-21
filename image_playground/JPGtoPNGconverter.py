import sys
import os
from PIL import Image

#grad the first and seconds argument
img_dir = sys.argv[1]
op_dir = sys.argv[2]

# check if new exists if not create
if not os.path.exists(op_dir):
    os.makedirs(op_dir)

#loop through the folder, convert each image to png
# save the png to new dir
for filename in os.listdir(img_dir):
    if filename.endswith(".jpg"):
        img = Image.open(f'{img_dir}{filename}')
        clean_name = os.path.splitext(filename)
        # print(clean_name)

        img.save(f'{op_dir}{clean_name[0]}.png', 'png')
        print("all done!")