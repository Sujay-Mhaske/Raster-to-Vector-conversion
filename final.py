
############################################################
# First converting image to binary
import cv2
img_grey = cv2.imread('2.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 128
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('binary.jpg', img_binary)

###############################################################
# Noting the coordinates of black points only
import numpy as np
from PIL import Image
import PIL

# image = Image.open("binary.jpg")
image = PIL.Image.open("binary.jpg")
image_data = np.asarray(image)

# width, height = image.size
# print(width, height)
# n=0

file = open('image.csv', 'w', encoding='utf-8')
for i in range(len(image_data)):
    for j in range(len(image_data[0])):
        # print(image_data[i][j][0], image_data[i][j][1], i, j)
        if image_data[i][j] < 10:
            file.write(str(i+1) + ',' + str(j+1))
            file.write('\n')
        # n+=1

# print(n)

###############################################################
# Adding consecutive points in a list and noting them
import csv
datafile = "image.csv"
data = list(csv.reader(open(datafile)))
# image = PIL.Image.open("binary.jpg")
# width, height = image.size
# print(width, height)

l1 = []
file = open('points.txt', 'a', encoding='utf-8')

for i in range(0, len(data)):
    a = data[i][1]
    b = int(a) + 1
    if int(data[i+1][1]) == b:
        l1.append(b)
    else:
        l1.clear()

    file.write(data[i][0] + ',' + str(l1))
    file.write('\n')
    # print(data[i][0], l1)

print('Done')