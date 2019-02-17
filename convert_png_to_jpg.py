from PIL import Image
import os
#
# this script converts all the images from png and JPG to jpg files
#
directory = 'data/img/'
directory1 = 'data/img1/'
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".png"):
        im = Image.open(directory + str(filename))
        rgb_im = im.convert('RGB')
        rgb_im.save(directory1 + str(filename[:-4]) + '.jpg')
        continue
    elif filename.endswith(".JPG"):
        im = Image.open(directory + str(filename))
        im.save(directory1 + str(filename[:-4]) + '.jpg')
        continue
    else:
        im = Image.open(directory + str(filename))
        im.save(directory1 + str(filename))
        continue