from math import sin,pi,cos
from pylab import figure ,subplot,plot,show,legend

t_end = 5
fs = 100
f =2
sig = []
dsig =[]
t_sig=[]

t = 0

while t <= t_end:
    x = sin(2*pi*t*f)
    dx = 2*pi*f*cos(2*pi*f*t)
    sig.append(x)
    dsig.append(dx)
    t_sig.append(t)
    t +=1/fs

figure()
plot(t_sig,sig,label = "f(t)")
plot(t_sig,dsig,color='g',label = 'f\'(t))')
legend()
show()