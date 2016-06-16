import random


def Bookie1(n,n1,n2):
    for i in range(2*n-n1-n2):
        D = random.randint(1,2)
        if D == 1:
            n1 += 1
        elif D == 2:
            n2 += 1
        if n1 == n:
            return 1
        elif n2 == n:
            return 2

def simulate1():
    n =100000
    win1 = 0
    win2 = 0
    for i in range(n):
        result = Bookie1(10,5,2)
        if result == 1:
            win1 += 1
        elif result == 2:
            win2 += 1
    print float(win1)/float(n)

def Bookie2(n,n1,n2):
    for i in range(2*n-n1-n2):
        D = random.randint(1,3)
        if D==1 or D==2:
            n1+=1
        elif D==3:
            n2+=1
        if n1 == n:
            return 1
        elif n2 == n:
            return 2

def simulate2():
    n = 100000
    win1 = 0
    win2 = 0
    for i in range(n):
        result = Bookie2(10,1,5)
        if result == 1:
            win1 +=1
        elif result == 2:
            win2 += 1
    print float(win1)/float(n)

simulate1()
simulate2()