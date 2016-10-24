# this program is to test whether python function by reference or by value
# version 1.1
# yanfguo@vub.ac.be 11Oct2016 17:04
from copy import deepcopy
a = 0
b = 2


def switchab(x, y):
    t = x
    x = y
    y = t


switchab(a, b)
print(a)
print(b)

# the result show that python is by value


# the code below is to test the copy difference

a = 'hello'
b = 'hello'
c = a
print [id(x) for x in [a, b, c]]

a = ['hello']
b = ['hello']
c = a
print [id(x) for x in [a, b, c]]

# this is because string is unchangeable, list is changeable.

a[0] = 'world'
print [id(x) for x in [a, b, c]]

a = 'world'
print [id(x) for x in [a, b, c]]

# shallow  copy  copy the address
a = ['hello', [1, 2, 3]]
b = a[:]
print [id(x) for x in [a, b]]
print [id(x) for x in a]
print [id(x) for x in b]


a[0] = 'world'
a[1].append([3, 4, 5])
print b
# deeply copy
b = deepcopy(a)
print [id(x) for x in [a, b]]
print [id(x) for x in a]
print [id(x) for x in b]

# link http://www.ahlinux.com/python/23153.html