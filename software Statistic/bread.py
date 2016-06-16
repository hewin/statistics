import numpy
import scipy.stats as sta
import matplotlib.pyplot as plt

X=sta.norm(loc=950,scale = 20)
wbread = []
for i in range(365):
    x=X.rvs(size = 100)
    wbread.append(max(x))

print numpy.mean(wbread)
print sta.skew(wbread)
plt.hist(wbread,color = 'gray')
plt.show()