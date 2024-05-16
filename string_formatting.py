# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:16:31 2022

@author: charl
"""

#  String Theory

print('%.3f' % (11/3))  # 3.667
print('%.2f' % (11/3))  # 3.67

print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))

print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))
name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
print(f'{name}, the {title}, is {reign}.')

hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7

x = float(input())
y = int(input())

print(f"{x:.{y}f}")
