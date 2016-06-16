import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm as N

def normal():
    x = np.linspace(-10,10,100)
    rv1 = N(0,1)
    rv2 = N(-5,1)
    rv3 = N(0,3)

    plt.plot(x,rv1.pdf(x),'green')
    plt.plot(x,rv1.cdf(x),'gray')
    plt.plot(x,rv2.pdf(x),'red')

    plt.plot(x,rv3.pdf(x),'blue')
    # plt.savefig(IMG_PATH + 'fig.png')
    plt.show()


normal()