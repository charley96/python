# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 17:57:35 2022

@author: charl
"""

abs_integer = abs(-10)  # 10
abs_float = abs(-10.0)  # 10.0

round_integer = round(10.0)      # 10, returns integer when ndigits is omitted
round_float = round(10.2573, 2)  # 10.26

pow_integer = pow(2, 10)  # 1024
pow_float = pow(2.0, 10)  # 1024.0

largest = max(1, 2, 3, 4, 5)   # 5
smallest = min(1, 2, 3, 4, 5)  # 1

import math

x = 2
y = 10
pow = math.pow(x, y)    # 1024.0
log = math.log(pow, x)  # 10.0
natural_log = math.log(1024)  # 6.931471805599453

import math

result = math.sqrt(100)  # 10.0

deg = 60.0
x = math.radians(deg)  # 1.047...

cos = math.cos(x)  # 0.500...
sin = math.sin(x)  # 0.866...

degrees = math.degrees(x)  # 59.999...