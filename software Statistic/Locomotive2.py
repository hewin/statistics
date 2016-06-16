#-*- coding :utf-8 -*-
import sys
import random

def number_trans(upper_bound):
    return random.randint(1, upper_bound)

def train_seen(N):
    return random.randint(1, N)

def MLE_estimation(evidence):
    return max(evidence)

def main():
    number_experience = 10000
    upper_bound = 100
    H1 = H2 = H3 = 0.0
    for j in range(number_experience):
        N = number_trans(upper_bound)
        evidence = range(100)[0:train_seen(N)+1]
        hypo1 = MLE_estimation(evidence)
        H1 = H1 + 1 if hypo1==N else H1
    print H1
    print H1/number_experience

if __name__ == '__main__':
    main()
