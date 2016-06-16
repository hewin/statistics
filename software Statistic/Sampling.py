#-*- coding:utf-8 -*-

import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import expon
import matplotlib.pyplot as plt

def sampling_distribution():
    fig, ax = plt.subplots(1, 1)
    x = np.linspace(-5,5,100)
    ax.plot(x,norm.pdf(x))

# 中心极限定理，样本均值服从正态分布（当样本足够大的时候）
    y = []
    n = 100
    for i in range(1000):
        r = expon.rvs(scale = 2 , size = 100)
        rsum = np.sum(r)
        z = (rsum - 100*2)/np.sqrt(4*100)
        y.append(z)
    ax.hist(y,normed = True,alpha=0.2)
    plt.show()

if __name__ == '__main__':
    sampling_distribution()