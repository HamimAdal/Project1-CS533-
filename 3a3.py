import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


lst=[]
x=[]
ser=[]
count=0

m = 2147483648
a = 37769685
c = 1
x0 = 1

prev_lcg=x0
x.append(x0)


n = 1000
for i in range(1,n):
    LCG = ((a*prev_lcg)+c) % m
    prev_lcg=LCG

    x.append(LCG)
    
for j in range(1,n):
    if x[j] != x[0]:
        count=count+1
    else:
        break


    
for j in range(1,n+1):
    ser.append(j)    

x_sample = np.array(ser)
y_sample = np.array(x)

plt.xlabel('X[i], where i= 1 to n')
# naming the y axis
plt.ylabel('value of random numbers in X[i], where i= 1 to n')

plt.title('Test 3, where m = 2147483648, a = 37769685, c = 1, x0 = 1')

plt.plot(x_sample, y_sample, label = "line 1")
plt.tight_layout()
plt.show()
