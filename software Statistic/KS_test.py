#-*- coding:utf-8 -*_
from scipy.stats import norm
from scipy.integrate import quad
import numpy as np
#双总体K-S检验
class Solution:
    def ks_test(self, f_obs):
        a = norm(loc = 577.6, scale = 56.37)
        



# f_obs
res = quad(np.sin, 0, np.pi/2)
print res
s = Solution()
s.ks_test([])

