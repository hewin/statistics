import matplotlib.pyplot as plt


def draw():
    DATA = [1,2,3,4,5,6,7,8,1,2,3,3,4,5,3,2,1,3,3]
    plt.boxplot(DATA)
    plt.show()

draw()