from pylab import *


def compare_img(img,color,threshold):
    newim =[[0 for j in range(len(img[0]))] for i in range(len(img))]
    for i in range(len(img)):
        for j in range(len(img[0])):
            if sum(abs(color-img[i][j]))<threshold:
                newim[i][j]=1
            else:
                newim[i][j]=1-(sum(abs(color-img[i][j]))-threshold)
    return newim


mario = imread("mario.png")
red1= imread("color1.png")
red = red1[0][0]
blue = imread("color2.png")[0][0]
figure(1)
imshow(compare_img(mario,red,0.01),cmap='gray')
title("threshold = 0.01,red")
figure(2)
imshow(compare_img(mario,red,0.5),cmap='gray')
title("threshold = 0.5,red")
show()

mario = imread("mario.png")
red1= imread("color1.png")
red = red1[0][0]
blue = imread("color2.png")[0][0]
figure(3)
imshow(compare_img(mario,blue,0.01),cmap='gray')
title("threshold = 0.01,blue")
figure(4)
imshow(compare_img(mario,blue,0.5),cmap='gray')
title("threshold = 0.5,blue")
show()


