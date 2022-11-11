# Getting the line before []
testsite_array = []
with open('points.txt') as my_file:
    for line in my_file:
        testsite_array.append(line)

with open('points2.csv', 'w') as my_file2:
    for i in range(0, len(testsite_array)):
        if ',[]' in testsite_array[i]:
            my_file2.write(testsite_array[i-1])

##############################################################
# Getting the first black point only
import csv

datafile = "points2.csv"
data = list(csv.reader(open(datafile)))
for i in range(0, len(data)):
    if data[i][1] != '[]':
        with open('points3.txt', 'a') as my_file3:
            my_file3.write(data[i][1] + ',' + data[i][0])
            my_file3.write('\n')


#############################################################
# Just removing [ or ] from the file
file = open("points3.txt", 'r')
Lines = file.readlines()
b = '[]'
for line in Lines:
    for char in b:
        line = line.replace(char, '')
    with open('points4.csv', 'a') as my_file4:
        my_file4.write(line)

############################################################
# Doing shift of coordinates from top left to bottom left
import csv
import PIL
from PIL import Image

image = PIL.Image.open("binary.jpg")
width, height = image.size

datafile = "points4.csv"
data = list(csv.reader(open(datafile)))
for i in range(0, len(data)):
    with open('points5.csv', 'a') as my_file5:
        a = height - int(data[i][1])
        my_file5.write(data[i][0] + ',' + str(a))
        # my_file5.write(str(width - int(data[i][0])) + ',' + str(a))
        my_file5.write('\n')