#-*- coding:utf-8 -*-

def F_One_Way(A1,A2,A3,A4,A5):
    fa = 4
    fb = 4 * 5 - fa - 1
    Sa = Cal_Sa(A1,A2,A3,A4,A5)
    Se = Cal_Se(A1,A2,A3,A4,A5)
    Va = Sa / fa
    Ve = Se / fb
    FA = Va / Ve
    return FA


def Cal_C(A1,A2,A3,A4,A5):
    sum = 0.0
    for i in range(len(A1)):
        sum += A1[i]
    for i in range(len(A2)):
        sum += A2[i]
    for i in range(len(A3)):
        sum += A3[i]
    for i in range(len(A4)):
        sum += A4[i]
    for i in range(len(A5)):
        sum += A5[i]
    return sum**2/(len(A1)+len(A2)+len(A3)+len(A4)+len(A5))

def Cal_Qt(A1,A2,A3,A4,A5):
    sum = 0.0
    for i in range(len(A1)):
        sum += A1[i]**2
    for i in range(len(A2)):
        sum += A2[i]**2
    for i in range(len(A3)):
        sum += A3[i]**2
    for i in range(len(A4)):
        sum += A4[i]**2
    for i in range(len(A5)):
        sum += A5[i]**2
    return sum


def Cal_Qa(A1,A2,A3,A4,A5):
    sum = 0.0
    tempSum = 0.0
    for i in range(len(A1)):
        tempSum += A1[i]
    sum += tempSum**2
    tempSum = 0.0

    for i in range(len(A2)):
        tempSum += A2[i]
    sum += tempSum**2
    tempSum = 0.0

    for i in range(len(A3)):
        tempSum += A3[i]
    sum += tempSum**2
    tempSum = 0.0

    for i in range(len(A4)):
        tempSum += A4[i]
    sum += tempSum**2
    tempSum = 0.0

    for i in range(len(A5)):
        tempSum += A5[i]
    sum += tempSum**2

    return sum/4


def Cal_St(A1,A2,A3,A4,A5):
    C = Cal_C(A1,A2,A3,A4,A5)
    Qt = Cal_Qt(A1,A2,A3,A4,A5)
    return Qt - C

def Cal_Sa(A1,A2,A3,A4,A5):
    Qa = Cal_Qa(A1,A2,A3,A4,A5)
    C = Cal_C(A1,A2,A3,A4,A5)
    return Qa - C

def Cal_Se(A1,A2,A3,A4,A5):
    St = Cal_St(A1,A2,A3,A4,A5)
    Sa = Cal_Sa(A1,A2,A3,A4,A5)
    return St - Sa

A1 = [25.6,22.2,28.0,29.8]
A2 = [24.4,30.0,29.0,27.5]
A3 = [25.0,27.7,23.0,32.2]
A4 = [28.8,28.0,31.5,25.9]
A5 = [20.6,21.2,22.0,21.2]

print Cal_C(A1,A2,A3,A4,A5)
print Cal_Qa(A1,A2,A3,A4,A5)
print Cal_Qt(A1,A2,A3,A4,A5)
print Cal_Sa(A1,A2,A3,A4,A5)
print Cal_St(A1,A2,A3,A4,A5)
print Cal_Se(A1,A2,A3,A4,A5)
print F_One_Way(A1,A2,A3,A4,A5)