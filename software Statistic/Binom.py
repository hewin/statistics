import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom as B

def binom():
    data = B(10,float(3)/float(4))
    x=np.arange(0,11,1)
    y=data.pmf(x)
    plt.bar(x,y,width=0.6,color='red')
    plt.show()

binom()