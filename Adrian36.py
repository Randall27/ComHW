#Name:  AdrianRandall
#Date:  October 2017
# 36

Import matplotlib.pyplot as plt
Import numpy as np

x = input (“”)
Y = input (“”)

Img = plt.imread(x)
height = img.shape (0)
width = img.shape(1)
img2 = img (height//2, hidth//2:) 

Plt.imsave (y, img2)
