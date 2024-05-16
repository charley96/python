# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:33:07 2022

@author: charl
"""
salary1 = int(input())

percent = 0
calculated_tax = round(salary1 * (percent / 100))
if 0 <= (salary1) <= 15527:
    percent = 0
    print(f'The tax for {salary1} is {percent}%. That is {calculated_tax} dollars!')
    
elif 15528 <= salary1 <= 42707:
    percent = 15
    calculated_tax = round(salary1 * (percent / 100))
    print(f'The tax for {salary1} is {percent}%. That is {calculated_tax} dollars!')
    
elif 42708 <= salary1 <= 132406:
    percent = 25
    calculated_tax = round(salary1 * (percent / 100))
    print(f'The tax for {salary1} is {percent}%. That is {calculated_tax} dollars!')
    
elif 132407 <= salary1:
    percent = 28
    calculated_tax = round(salary1 * (percent / 100))
    print(f'The tax for {salary1} is {percent}%. That is {calculated_tax} dollars!')
