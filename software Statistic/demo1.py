#-*- coding:utf-8 -*-
import matplotlib.pyplot as p
from math import sqrt
from math import pow

def drange(start,stop,step):
	r = start
	while r<stop:
		yield r
		r += step


def func1(x):
	a = sqrt(255.0/17 - 255*pow(x,2)/289)
	return a

def func2(x):
	b = 8.0/17 * x
	return b


xrange0 = drange(0,sqrt(17),0.001)
xrange1 = drange(-1*sqrt(17),0,0.001)

xindex0 = []
xindex1 = []
y1 = []
y2 = []
y3 = []
y4 = []

for x in xrange0:
	xindex0.append(x)
	y3.append(-1 * func1(x) + func2(x))
	y1.append(func1(x) + func2(x))

for x in xrange1:
	xindex1.append(x)
	y2.append(func1(x) - func2(x))
	y4.append(-1*func1(x) - func2(x))


p.plot(xindex0,y1,xindex0,y3,xindex1,y2,xindex1,y4,c='r')
x
p.show()