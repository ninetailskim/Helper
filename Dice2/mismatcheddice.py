import random
import time
import numpy as np

def dices(n_rolls,dices):
    N_dices=len(dices)
    sides=dices
    n=n_rolls
    max=np.sum(dices)
    min=N_dices
    counting=np.zeros(max-min+1)+N_dices #sum of everydices each time
    histogram_count=np.zeros(max-min+1)
    for i in range(0,len(counting)):
        counting[i]=counting[i]+i
    print(counting)
    print(histogram_count)
    
    for i in range(0,n): #for roll dices n time
        sum = np.sum([int(np.random.random() * x) for x in dices])
        histogram_count[sum]=histogram_count[sum]+1
    print("the result of sums =",histogram_count)

    mean = 0
    variance = 0
    for i in range(len(counting)):
        mean += 1.0 * counting[i] * histogram_count[i] / n
    for i in range(len(counting)):
        variance += 1.0 * (counting[i] -  mean) ** 2 * histogram_count[i] / n
    print(mean)
    print(variance)
    deviation = variance ** 0.5
    print(deviation)

def run():
    dices(10000,[4,6])
run()





