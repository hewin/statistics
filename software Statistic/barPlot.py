import sys
import numpy as np
import matplotlib.pyplot as plt

def get_data():
    mu = 100
    sigma = 15
    x = mu + sigma * np.random.randn(10000)
    return x

def draw(IMG_PATH):
    x = get_data()
    # print 'the data is : '+ str(x)
    plt.hist(x,bins=50,color='g',alpha=0.5)
    plt.show()
    # plt.savefig(IMG_PATH)



draw('e:/CODE/python'+'.png')