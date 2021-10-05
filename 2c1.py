import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
min_range = 2
max_range = 10
x=[]

m = 126
a = 43
c = 2
x0 = 2

prev_lcg=x0
x.append(x0)

n = 100 
for i in range(1,n):
    LCG = ((a*prev_lcg)+c) % m
    LCG = (LCG % (max_range-min_range+1)) + min_range
    prev_lcg=LCG
    x.append(LCG)  
print (x)

