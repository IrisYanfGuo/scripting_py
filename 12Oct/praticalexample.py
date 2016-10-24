from pylab import *

global g  # the gravity
g = 9.81


def projectile_motion(alfa, v0, frequency):
    point = int(1/frequency)
    x=[]
    y=[]
    for i in range(point):
        x.append(v0 * frequency * i * cos(alfa/180*math.pi))
        y.append(v0 * frequency * i * sin(alfa/180*math.pi) - 0.5 * g * (i * frequency)**2)
    return  x,y

x, y = projectile_motion(30, 10, 0.01)

figure()
plot(x,y)
show()

# finally finished
# how to sync
