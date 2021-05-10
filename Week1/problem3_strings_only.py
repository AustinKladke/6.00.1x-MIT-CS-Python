# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 08:43:20 2021

@author: akladke
"""

s = 'azcbobobegghakl'

current_sub_str = ""

for i in range(len(s)):
    sub_str = s[i:]
    new_sub_str = ""
    for j in range(len(sub_str)):
        if j + 1 < len(sub_str) and sub_str[j] <= sub_str[j+1]:
            new_sub_str += sub_str[j]
        else:
            new_sub_str += sub_str[j]
            break
    if len(new_sub_str) > len(current_sub_str):
        current_sub_str = new_sub_str
        
print("Longest substring in alphabetical order: " + current_sub_str)