import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import random


x=[]
bar_head=[]
bar_tail=[]

head=0
tail=0

def mean_calc(m,a,c,prev_lcg,n):
    head=0
    tail=0
    x.append(prev_lcg)
    #sum_calc=prev_lcg
    for i in range(1,n):
        LCG = ((a*prev_lcg)+c) % m
        prev_lcg=LCG
        x.append(LCG)
      
    for j in range(1,n+1):
        pick=random.choice(x)
        #print(pick)
        if pick == 0:
            tail=tail+1
        elif pick ==1:
            head=head+1
    
    avg_head=head/n
    avg_tail=tail/n
    print("Average head")
    print(avg_head)
    print("Average tail")
    print(avg_tail)
    print("\n")

    bar_head.append(avg_head)
    bar_tail.append(avg_tail)
    
    x.clear()
    
mean_calc(2,43,25,1,10)
mean_calc(2,43,25,1,100)
mean_calc(2,43,25,1,1000)
mean_calc(2,43,25,1,10000)
mean_calc(2,43,25,1,1000000)




# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize =(12, 8))
 
# Set position of bar on X axis
br1 = np.arange(len(bar_head))
br2 = [x + barWidth for x in br1]

 
# Make the plot
plt.bar(br1, bar_head, color ='r', width = barWidth,
        edgecolor ='grey', label ='Head')
plt.bar(br2, bar_tail, color ='g', width = barWidth,
        edgecolor ='grey', label ='Tail')

 
# Adding Xticks
plt.xlabel('Sample Size', fontweight ='bold', fontsize = 15)
plt.ylabel('Probability', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(len(bar_head))],
        ['10', '100', '1000', '10000', '100000'])
 
plt.legend()
plt.show()


