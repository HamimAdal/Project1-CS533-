import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

deci=[]
min_range =-100
max_range = 100
x=[]
m = 126
a = 43
c = 25
x0 = 25

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
print (deci)

