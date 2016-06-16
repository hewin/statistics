#-*- coding:utf-8 -*-

import numpy as np

def twoway_anova(A):
    C = np.sum(A)**2/24
    As = np.sum(A, axis=1)
    Ab = np.sum(A, axis=0)

    Qt = 0.0
    for i in range(4):
        for j in range(6):
            Qt += A[i][j]**2
    St = Qt - C

    Qa = 0.0
    for i in range(4):
        Qa += As[i]**2
    Sa = Qa/6 - C

    Qb = 0.0
    for i in range(6):
        Qb += Ab[i]**2
    Sb = Qb/4 - C
    Se = St - Sa -Sb

    Va = Sa / 3
    Vb = Sb / 5
    Ve = Se / 15
    return (Va,Vb,Ve)






A1 = [0.05,0.46,0.12,0.16,0.84,1.3]
A2 = [0.08,0.38,0.4,0.1,0.92,1.57]
A3 = [0.11,0.43,0.05,0.1,0.94,1.1]
A4 = [0.11,0.44,0.08,0.03,0.93,1.15]
A = [A1,A2,A3,A4]
print len(A)

def main():
    pass

if __name__ == '__main__':
    print twoway_anova(A)