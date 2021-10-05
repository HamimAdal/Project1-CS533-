import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

x=[]
deci=[]
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
    prev_lcg=LCG

    x.append(LCG)
    deci.append(round(LCG/m, 2))
print (deci)
