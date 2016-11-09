from pylab import figure, title, subplot, plot, show
from numpy import median
f = open('sig1.txt', 'r')
sig1 = []

for line in f:
    sig1.append(float(line.strip()))
f.close()

f = open('sig2.txt', 'r')
sig2 = []

for line in f:
    sig2.append(float(line.strip()))
f.close()

figure()
subplot(2,1,1)
plot(sig1)
title("sig1")



def filter(list1, h):
    list2 = []
    for i in range(h - 1, len(list1)):
        tlist = list1[i + 1 - h:i + 1]
        list2.append(sum(tlist) / h)
    return list2

def filter_median(list1,h):
    list2 = []
    for i in range(h-1,len(list1)):
        tlist = list1[i+2-h:i+1]
        list2.append(median(tlist))
    return list2


figure(1)

filt1 = filter(sig1, 6)
subplot(2,1,2)
plot(sig1)
plot(filt1,color = 'r')
title("filt1 with sig1")

subplot(2,1,1)
plot(sig2)
title("filter 1 with sig2")
plot(filter(sig2,2),color='r')



figure(2)
filt1 = filter_median(sig1, 6)
subplot(2,1,2)
plot(sig1)
plot(filt1)
title("filt2")

subplot(2,1,1)
plot(sig2)
title("sig2")
plot(filter(sig2,2),color='r')
show()