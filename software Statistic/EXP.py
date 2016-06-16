import math
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon as E

def exp(lam):
    p=random.random()
    return -math.log(1-p)/lam

x1=[]
for i in range(100):
    x1.append(exp(1))
x1 = sorted(x1)
y1 = np.linspace(0,1,100)
plt.plot(x1,y1,color='red')
rv = E(1)
x2=np.linspace(0,5,100)
plt.plot(x2,rv.cdf(x2),color='blue')
plt.show()