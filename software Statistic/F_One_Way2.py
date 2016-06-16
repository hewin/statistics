#-*- coding:utf-8 -*-

import numpy as np

class Solution:
    def F_One_Way(self,A):
        n = 20
        As = np.sum(A, axis = 1)
        QA = 0.0
        for i in range(4):
            QA = QA + As[i]**2
        QA = QA / 5
        QT = 0.0
        for i in range(4):
            for j in range(5):
                QT += A[i][j]**2
        C = np.sum(A)**2/n
        ST = QT - C
        SA = QA - C
        Se = ST - SA
        F = (SA/3)/(Se/16)
        return F


A1 = [27.0,26.2,28.8,33.5,28.8]
A2 = [22.8,23.1,27.7,27.6,24.0]
A3 = [21.9,23.4,20.1,27.8,19.3]
A4 = [23.5,19.6,23.7,20.8,23.9]
A = [A1,A2,A3,A4]
print Solution().F_One_Way(A)