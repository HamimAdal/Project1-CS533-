import numpy as np
import numpy.random as rd
from scipy import stats
import matplotlib.pyplot as plt
import random


def lcg(m,a,c,x0):
    deci=[]
    min_range =-100
    max_range = 100
    x=[]

    prev_lcg=x0
    x.append(x0)
    deci.append(round(x0/m, 2))
    n = 100 
    for i in range(1,n):
        LCG = ((a*prev_lcg)+c) % m
        LCG = (LCG % (max_range-min_range+1)) + min_range
        prev_lcg=LCG
        x.append(LCG)  
        deci.append(round(LCG/m, 2))
    #print (deci)
    return deci

def X1_function(V1, W):

    Y = np.sqrt(-2 * np.log(W) /W)
    X1 = V1 * Y
    return X1

def polar_method(N):
    out = np.zeros(N)
    for i in range (N):
        W = 2
        while W > 1:
            V1 = random.choice(lcg(126,43,25,25))
            V2 = random.choice(lcg(126,43,25,25))
            W = V1**2 + V2**2
        X = X1_function(V1, W)
        out[i]= X
    return out

X= polar_method(100000)
plt.figure()
plt.hist(X, bins = 50, density=True)
xx= np.linspace(-8,8,100)
plt.plot(xx, stats.norm.pdf(xx))
plt.show()




