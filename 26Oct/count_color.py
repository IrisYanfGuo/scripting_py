from pylab import *


def count_color(img,color,threshold):
    newim =[[0 for j in range(len(img[0]))] for i in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            if color[0]-img[i][j][0]<threshold:
                newim[i][j]=1
            else:
                newim[i][j]=1-(color[0]-img[i][j][0]-threshold)
    return newim


mario = imread("mario.png")
red1= imread("color1.png")
red = red1[0][0]
blue = imread("color2.png")[0][0]
figure(1)
imshow(count_color(mario,red,0.01),cmap='gray')
title("threshold = 0.1,red")
figure(2)
imshow(count_color(mario,red,0.9),cmap='gray')
title("threshold = 0.5,red")
show()


