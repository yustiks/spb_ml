# script for YOLO neural network bounding box convertion
# input is the x, y, w, h
# x, y - coordinates for left-bottom of the bounding box,
# w, h - width and height of bounding box
# output is xc, yc, w, h
# xc, yc - center of the bounding box
# w, h - width and height for bounding box
import cv2
img_name = str(input('input img name: '))
x, y, w, h, cl = map(int, input('input x, y, w, h, class of the box in the pixels: ').split())
# [category number] [object center in X] [object center in Y] [object width in X] [object width in Y]
img = cv2.imread(img_name + '.JPG')
file = open(img_name + '.txt', 'w')
real_height, real_width, _ = img.shape
xc = round((x + w/2)/real_width, 2)
yc = round((y + h/2)/real_height, 2)
wbox = round(w/real_width, 2)
hbox = round(h/real_height, 2)
file.write(str(cl) + ' ' + str(xc) + ' ' + str(yc) + ' ' + str(wbox) + ' ' + str(hbox))
file.close()
print('file was written')