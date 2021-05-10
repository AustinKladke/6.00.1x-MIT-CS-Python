# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:55:31 2021

@author: akladke
"""

temp = 120
if temp > 85:
    print("Hot")
elif temp > 100:
    print("REALLY HOT!")
elif temp > 60:
    print("Comfortable")
else:
    print("Cold")
    
# Experiment results: if and elif actually are different from
# each other! An if statement will get executed, an elif statement
# will not in the above situation (if another if or elif statement
# has been triggered already)