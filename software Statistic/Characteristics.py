#-*- coding:utf-8 -*-
import codecs
import numpy as np
from scipy import integrate
from scipy.stats import binom
from scipy.stats import expon
from scipy.stats import norm

def nc_of_binom():
    rv = binom(10,0.2)
    print '(平均值:%d)' % rv.mean()
    print '(方差： %d)' % rv.var()
    # print rv.moment(3)

def nc_of_expon():
    E1 = lambda x : x*0.5*np.exp(-x/2)
    E2 = lambda x : x**2*0.5*np.exp(-x/2)
    print integrate.quad(E1, 0, np.inf)
    print integrate.quad(E2, 0, np.inf)
    print expon(scale=2).moment(1)
    print expon(scale=2).var()

def nc_of_norm():
    rv = norm(loc = 1,scale = 3)
    print rv.mean()
    print rv.var()


# nc_of_binom()
nc_of_expon()
# nc_of_norm()