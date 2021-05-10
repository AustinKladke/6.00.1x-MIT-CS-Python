# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:45:02 2021

@author: akladke
"""

s = "azcbobobegghakl"

count = 0
for i in s:
    if i in "aeiou":
        count += 1
print("Number of vowels: " + str(count))