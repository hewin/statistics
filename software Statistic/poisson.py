import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson as Pie

def poisson_pmf():
    rv=Pie(4.5)
    x=np.arange(0,11,1)
    y=rv.pmf(x)

    plt.bar(x,y,width=0.6,color='red')
    plt.show()


poisson_pmf()