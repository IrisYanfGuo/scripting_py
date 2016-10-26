from pylab import *

# yanfguo@vub.ac.be  by Iris Yanfang Guo
# Oct 26th 2016

img = imread("coins.png")
print(img)
#imshow(img,cmap='gray')
#show()
print(len(img),len(img[0]))


def derivative(alist):
    rlist=[alist[0]]
    for i in range(len(alist)-1):
        rlist.append(alist[i+1]-alist[i])
    return rlist



threshold=0.05
def edgeDect(img):
    lx=[]
    ly=[]
    img_grad=[]
    for row in img:
        lx.append(derivative(row))

    for i in range(len(img)):
        temp=[]
        for j in range(len(img[0])):
            temp.append(img[i][j])
        ly.append(derivative(temp))

    for i in range(len(img)):
        t = []
        for j in range(len(img[0])):
            t.append(lx[i][j]**2+ly[i][j]**2)
        img_grad.append(t)
    img_edges=[]
    for i in range(len(img_grad)):
        t=[]
        for j in range(len(img_grad[0])):
            if img_grad[i][j]<threshold:
                t.append(0)
            else:
                t.append(1)
        img_edges.append(t)
    return img_edges


imshow(edgeDect(img),cmap='gray')
show()
