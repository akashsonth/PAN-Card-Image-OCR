from __future__ import print_function
from file_read_backwards import FileReadBackwards
from pytesseract import image_to_string
from PIL import Image
import numpy as np
import sys


#Convert image to Black & White

im=Image.open('test.jpg','r')

im=im.convert('L') #makes it greyscale
bw = im.point(lambda x: 0 if x<75 else 255, '1')
bw.save("test_bw.jpg")

im = Image.open("test_bw.jpg")

#im = Image.open("test.jpg")

#print(im)


#Print the text extracted

x = (image_to_string(im)).encode('ascii', 'ignore')
#print(x)
f = open('test.txt', 'w')
f.write(x)
f.close()

f = FileReadBackwards('test.txt')


#Get only the PAN number

nc = 0
for line in f:
    if nc==10:
        print(s)
        break
    nc = 0
    s = ""
    for ch in line:
        if (ch<='Z' and ch>='A') or (ch<='9' and ch>='0') :
            nc = nc + 1
            s = s + ch
            #print(ch,end='')
        else:
            continue
