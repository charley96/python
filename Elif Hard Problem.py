# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 18:57:47 2022

@author: charl
"""
import math
chicken = 23 
goat = 678 
pig = 1296
cow = 3848
sheep = 6769

money = int(input())
a = money / sheep
b = money / cow
c = money / pig
d = money / goat
e = money / chicken
if a >= 1:
    print(str(math.floor(a)) + " sheep")

elif 1 <= b < 2:
    print(str(math.floor(b)) + " cow")
elif b >= 2:
    print(str(math.floor(b)) + " cows")
    
elif 1 <= c < 2:
    print(str(math.floor(c)) + " pig")
elif c >= 2:
    print(str(math.floor(c)) + " pigs")
    
elif 1 <= d < 2:
    print(str(math.floor(d)) + " goat")
elif d >= 2:
    print(str(math.floor(d)) + " goats")

elif 1 <= e < 2:
    print(str(math.floor(e)) + " chicken")
elif e >= 2:
    print(str(math.floor(e)) + " chickens")
    
else:
    print("None")
