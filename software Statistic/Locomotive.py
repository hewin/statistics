#-*- coding:utf-8 -*-

# 火车头问题
import random


def number_trans(upper_bound):
    return random.randint(1,upper_bound)

def train_seen(N):
    return random.randint(1,N)

# 最大似然估计，即概率最大
def MLE_estimation(evidence):
    return evidence

# 偏差平方和最小
def MSE_estimation(evidence):
    return round(1.5*evidence)

# 偏差最小
def ME_estimation(evidence):
    return 2*evidence

def main():
    number_experiments =10000
    upper_bound = 100
    H1=H2=H3=MSE1=MSE2=MSE3=ME1=ME2=ME3=0.0
    for i in range(number_experiments):
        N = number_trans(upper_bound)
        evidence = train_seen(N)

        hypo1 = MLE_estimation(evidence)
        hypo2 = MSE_estimation(evidence)
        hypo3 = ME_estimation(evidence)

        H1=H1+1 if hypo1==N else H1
        H2=H2+1 if hypo2==N else H2
        H3=H3+1 if hypo3==N else H3

        MSE1 = MSE1 + (hypo1-N)**2
        MSE2 = MSE2 + (hypo2-N)**2
        MSE3 = MSE3 + (hypo3-N)**2

        ME1 = ME1 + (hypo1-N)
        ME2 = ME2 + (hypo2-N)
        ME3 = ME3 + (hypo3-N)

    print H1/number_experiments,H2/number_experiments,H3/number_experiments
    print MSE1/number_experiments,MSE2/number_experiments,MSE3/number_experiments
    print ME1/number_experiments,ME2/number_experiments,ME3/number_experiments

main()