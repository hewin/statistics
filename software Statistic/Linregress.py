#-*- coding:utf-8 -*-
# 计算线性回归方程

import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def linregress1():
    x = np.linspace(-5, 5, 150)
    y = x + np.random.normal(size = x.size)
    y[12:14] += 10
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    lxx = 0.0
    lxy = 0.0
    for i in range(len(x)):
        lxx += (x[i] - x_mean)**2
    for i in range(len(x)):
        lxy += (x[i]-x_mean)*(y[i]-y_mean)
    b = lxy/lxx
    a = y_mean - b*x_mean

    st = 0.0
    for i in range(len(x)):
        st += (y[i] - y_mean)**2
    sr = 0.0
    for i in range(len(x)):
        sr += (x[i]*b + a - y_mean)**2
    se = 0.0
    for i in range(len(x)):
        se += (x[i]*b + a - y[i])**2
    F = sr/se*(len(x) - 2)
    stderr = np.sqrt(se/(len(x)-2))
    r = np.sqrt(sr/st)
    print (sr,se,st)
    # print stats.linregress(x,y)
    return (b,a,r,stderr)

def main():
    pass

if __name__ == '__main__':
    print linregress1()
