# this script take one object from the image and create different locations for it in different background
import cv2
#img_name = str(input('input img name: '))
img_name = 'img_3'
img = cv2.imread(img_name + '.JPG')
with open(img_name + '.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
for i in range(len(content)):
    cl, xc, yc, wbox, hbox = map(float, content[i].split())
    print(cl, xc, yc, wbox, hbox)
    real_height, real_width, _ = img.shape
    print('real_height ', real_height)
    print('real_width ', real_width)
    x_bottom = int((xc - wbox/2) * real_width)
    print('x_bottom ' , x_bottom)
    y_bottom = int((yc - hbox/2) * real_height)
    print('y_bottom ', y_bottom)
    x_top = int((xc + wbox/2) * real_width)
    print('x_top ', x_top)
    y_top = int((yc + hbox/2) * real_height)
    print('y_top ', y_top)
    img_small = img[y_bottom:y_top, x_bottom:x_top]
    cv2.imwrite('object.jpg', img_small)