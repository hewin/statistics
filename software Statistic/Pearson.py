#-*- coding:utf-8 -*-

import numpy as np
from scipy import stats

def pearsonr():
    x = np.linspace(-5, 5, num = 150)
    y = x + np.random.normal(size=x.size)
    # y[12:14] += 10
    print stats.pearsonr(x, y)
    sum_1 = 0.0
    for i in range(len(x)):
        sum_1 += (x[i]-np.mean(x))*(y[i]-np.mean(y))
    sum_2 = 0.0
    for i in range(len(x)):
        sum_2 += (x[i]-np.mean(x))**2
    sum_3 = 0.0
    for i in range(len(y)):
        sum_3 += (y[i]-np.mean(y))**2
    r = sum_1/(np.sqrt(sum_2)*np.sqrt(sum_3))
    return r




def main():
    pass

if __name__ == '__main__':
    print pearsonr()

