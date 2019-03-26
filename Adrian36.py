#Name:  AdrianRandall
#Date:  October 2017
# 36

Import matplotlib.pyplot as plt
Import numpy as np

x= input (“”)
Y = input (“”)

Img = plt.imread(x)
Height = img.shape (0)
Width = img.shape(1)
Img2 = img (Height//2, Width//2:) 

Plt.imsave (y,img2)
