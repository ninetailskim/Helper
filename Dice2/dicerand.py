import random
import time
import numpy as np

def dices():
    c1=time.clock()
    N_dices=int(input(">>>How many dices:"))
    sides=int(input(">>>sides :"))
    n=int(input(">>>n rolls :"))
    max=N_dices*sides
    min=N_dices
    histogram=np.zeros((N_dices,sides))
    counting=np.zeros(max-min+1)+N_dices #sum of everydices each time
    histogram_count=np.zeros(max-min+1)
    for i in range(0,len(counting)):
        counting[i]=counting[i]+i
    print(counting)
    print(histogram_count)

    
    for i in range(0,n): #for roll dices n time
        sum=0
        for j in range(0,N_dices): #with N_dices each time
            one_dice=int(np.random.random()*sides)#each dice number
            #np.random.randint(sides)+1(not pass 
            histogram[j,one_dice]=histogram[j,one_dice]+1
            sum=sum+one_dice
        histogram_count[sum]=histogram_count[sum]+1
    print(histogram)

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
            dices()
run()





