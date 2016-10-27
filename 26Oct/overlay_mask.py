# this is a program show overlay and mask of two images# yanfguo@vub.ac.befrom  pylab import *from numpy import *img1 = imread('python.png')img2 = imread('bugs.png')mask = imread('bugs_mask.png')def img2list(img):    out =[]    for i in img:        t= []        for j in i:            t.append(j)        out.append(j)    return out# blending factoralpha = 0.5# img1 and img2 are the same sizedef overlay(img1, img2):    out = []    for i in range(len(img1)):        t = []        for j in range(len(img1[0])):            t.append(alpha * img1[i][j] + (1 - alpha) * img2[i][j])        out.append(t)    return outimshow(overlay(img1, img2))# show()# using a mask, modify overlay# problems appear how to detect a img's color is blackdef overlay_mask(img1, img2):    out = []    for i in range(len(img1)):        t = []        for j in range(len(img1[0])):            if mask[i][j].all()!=1:                t.append(img2[i][j])            else:                t.append(img1[i][j])        out.append(t)    return outimshow(overlay_mask(img1, img2))show()