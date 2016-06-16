#-*- coding:utf-8 -*-

import sys
import numpy as np
from scipy.stats import norm
from scipy.stats import chi2
import matplotlib.pyplot as plt

def chi2_distribution():
    fig,ax = plt.subplots(1, 1)
    df = 10
    x=np.linspace(chi2.ppf(0.01, df),chi2.ppf(0.99, df), 100)
    ax.plot(x, chi2.pdf(x,df))

    y = []
    n=10
    for i in range(1000):
        chi2r = 0.0
        r = norm.rvs(size = 10)
        for j in range(10):
            chi2r = chi2r + r[j]**2
        y.append(chi2r)
    ax.hist(y, normed=True, alpha=0.2)
    plt.show()

# def main():
#     pass

if __name__ == '__main__':
    chi2_distribution()

