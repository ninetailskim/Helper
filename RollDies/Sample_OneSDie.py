import random
import time
import numpy as np

def OneDieS_np(trials, sides, show=False):
    if show:
        c1=time.clock()
        print("====================")
        print("Number of sides = ", sides)
        print("Number of trials = ", trials)

    histogram = np.zeros(sides)
    if show:
        print(histogram)

    r = 0
    for t in range(trials):
        r = int(np.random.random()*sides)
        histogram[r] = histogram[r] + 1
    if show:
        print(histogram)

    if show:
        print("s, N_s, N_s-N/sides, N_s/N, N_s/N-1/sides")
        for s in range(sides):
            print(s+1, histogram[s], histogram[s]-trials/sides, histogram[s]/trials, histogram[s]/trials-1/sides)
    if show:
        c2=time.clock()
        print("Elapsed time =", c2-c1)
    return histogram

def run():
    sides = int(input('input the Side '))
    trials = 100000
    result = OneDieS_np(trials, sides, True)
    mean = 0
    vari = 0
    #experiment
    for i in range(sides):
        mean += (i + 1) * result[i]/trials
        
    for i in range(sides):
        vari += (i + 1 - mean) ** 2 * result[i] / trials

    dev = vari ** (0.5)
    print(sides," sides die and ", trials, "trials:")
    print("experiment result:")
    print('mean:',mean ,' variance:',vari, ' standdev:', dev)

    #theoretical
    the_mean = 0
    the_vari = 0
    for i in range(sides):
        the_mean += 1.0 * (i + 1) * 1 / sides

    for i in range(sides):
        the_vari += 1.0 * (i + 1 - the_mean) ** 2 / sides
    
    the_dev = the_vari ** (0.5)
    print("theoretical result:")
    print('mean:',the_mean ,' variance:',the_vari, ' standdev:', the_dev)

    print("error:")
    print('mean error:',abs(the_mean - mean) / the_mean,' variance error:',abs(the_vari - vari)/the_vari, ' standdev error:', abs(the_dev - dev)/the_dev)
    print("error for each side:")
    for i in range(sides):
        print(i + 1,":", abs(result[i] - trials/sides) / (trials/sides))

run()
