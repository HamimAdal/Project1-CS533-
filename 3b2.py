import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random

total = [0] * 12
x=[]
bar_head=[]
bar_tail=[]

head=0
tail=0

def mean_calc(m,a,c,prev_lcg,n):
    head=0
    tail=0

    for i in range(1,n):
        LCG = ((a*prev_lcg)+c) % m
        prev_lcg=LCG
        x.append(LCG)
      
    for j in range(1,n+1):
        pick1=random.choice(x)
        pick2=random.choice(x)
        total_value=pick1+pick2
        total[total_value]=total[total_value]+1 
        
    x.clear()
    plt.bar([1,2,3,4,5,6,7,8,9,10,11,12], total, color ='r')   
    plt.xlabel('Sample Size %i'%n, fontweight ='bold', fontsize = 15)
    plt.ylabel('number of occurence', fontweight ='bold', fontsize = 15)
    plt.show()
    
mean_calc(6,43,25,1,10)
mean_calc(6,43,25,1,100)
mean_calc(6,43,25,1,1000)
mean_calc(6,43,25,1,10000)
mean_calc(6,43,25,1,1000000)





