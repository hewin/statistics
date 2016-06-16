import numpy as np
import matplotlib.pyplot as plt

def get_data():
    mu = 100
    sigma = 15
    x = mu + sigma*np.random.randn(100)
    return x

def draw():
    x = get_data()

    plt.plot(x,'r--')

    plt.show()

draw()