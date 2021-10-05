import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

lst1=[]
x1=[]

m1 = 9
a1 = 4
c1 = 2
x0_1 = 2

prev_lcg1=x0_1
x1.append(x0_1)

n = 5678

for i in range(1,n+1):
    LCG1 = ((a1*prev_lcg1)+c1) % m1
    prev_lcg1=LCG1
    x1.append(LCG1)
    
#print (x1)
lst2=[]
x2=[]

m2 = 126
a2 = 43
c2 = 25
x0_2 = 25

prev_lcg2=x0_2
x2.append(x0_2)



for i in range(1,n+1):
    LCG2 = ((a2*prev_lcg2)+c2) % m2
    prev_lcg2=LCG2
    x2.append(LCG2)
    
#print (x2)


lst3=[]
x3=[]

m3 = 120
a3 = 49
c3 = 31
x0_3 = 26

prev_lcg3=x0_3
x3.append(x0_3)



for i in range(1,n+1):
    LCG3 = ((a3*prev_lcg3)+c3) % m3
    prev_lcg3=LCG3
    x3.append(LCG3)
    
change =1  # switching=1 , not switching = 0

change_loss=0
not_change_loss=0

change_count=0
not_change_count=0


for i in range(1,n+1):

    winner = (x1[i] % 3)+1  #1
    picked = (x2[i] % 3)+1  #1


    if winner == 1 and picked == 1:
        revealed= (x3[i] % 2)+2  #1
        if revealed == 2: 
            if change == 0:
                picked=1 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=3
                change_loss=change_loss+1
                
        elif revealed ==3:
            if change == 0:
                picked=1 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=2
                change_loss=change_loss+1
                

    elif winner == 1 and picked == 2:
        revealed= 3
        if change == 0:
            picked=2
            not_change_loss=not_change_loss+1
           
        elif change == 1:
            picked=1 #winner
            change_count=change_count+1
    

    elif winner == 1 and picked == 3:
        revealed= 2
        if change == 0:
            picked=3
            not_change_loss=not_change_loss+1            
        elif change == 1:
            picked=1 #winner
            change_count=change_count+1
    

    elif winner == 2 and picked == 1:
        revealed= 3
        if change == 0:
            picked=1
            not_change_loss=not_change_loss+1
        
        elif change == 1:
            picked=2 #winner
            change_count=change_count+1

    
    elif winner == 2 and picked == 2:
        revealed= (x3[i] % 2)  
        if revealed ==0: #1
            if change == 0:
                picked=2 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=3
                change_loss=change_loss+1
             
        elif revealed ==1: #3
            if change == 0:
                picked=2 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=1
                change_loss=change_loss+1
             

    elif winner == 2 and picked == 3:
        revealed= 1
        if change == 0:
            picked=3
            not_change_loss=not_change_loss+1
           
        elif change == 1:
            picked=2 #winner
            change_count=change_count+1


    elif winner == 3 and picked == 1:
        revealed= 2
        if change == 0:
            picked=1
            not_change_loss=not_change_loss+1
           
        elif change == 1:
            picked=3 #winner
            change_count=change_count+1


    elif winner == 3 and picked == 2:
        revealed= 1
        if change == 0:
            picked=2
            not_change_loss=not_change_loss+1
           
        elif change == 1:
            picked=3 #winner
            change_count=change_count+1

    
    elif winner == 3 and picked == 3:
        revealed= (x3[i] % 2) +1   
        if revealed ==0:
            if change == 0:
                picked=3 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=2
                change_loss=change_loss+1
              
        elif revealed ==1: 
            if change == 0:
                picked=3 #winner
                not_change_count=not_change_count+1
            elif change == 1:
                picked=1
                change_loss=change_loss+1
              

if change == 0:
    print('Won by not switching:')
    print(not_change_count)
    print('Loss by not switching:')
    print(not_change_loss)
    not_change_win_per=not_change_count/(not_change_loss + not_change_count)
    print('Probability of winning while not switching:')
    print(not_change_win_per)

elif change == 1:
    print('Won by switching:')
    print(change_count)
    print('Loss by switching:')
    print(change_loss)
    change_win_per=change_count/(change_loss + change_count)
    print('Probability of winning while switching:')
    print(change_win_per)
