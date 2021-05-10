# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:53:39 2021

@author: akladke
"""

s = "azcbobobegghakl"

count = 0
for i in range(len(s)):
    if s[i:i+3] == "bob":
        count += 1
print("Number of times bob occurs is: " + str(count))
    