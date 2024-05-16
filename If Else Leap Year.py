# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 16:18:04 2022

@author: charl
"""

year = int(input())

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("Leap")
else:
    print("Normal")
    

A = int(input())  # Minimum Sleep
B = int(input())  # Maximum Sleep
H = int(input())  # Actual Sleep

if A <= H <= B:
    print("Normal")
if A > H:
    print("Deficiency")
if H > B:
    print("Excess")