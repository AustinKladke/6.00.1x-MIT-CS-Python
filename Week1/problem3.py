# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:09:52 2021

@author: akladke
"""

overall_lst = []

s = 'azcbobobegghakl'

for i in range(len(s)):
    sub_str = s[i:]
    sub_str_lst = [] # List gets reset after inner loop is broken out of
    current_sub_str = "" # String gets reset after inner loop is broken out of
    for j in range(len(sub_str)):
        if j + 1 < len(sub_str) and sub_str[j] <= sub_str[j+1]:
            current_sub_str += sub_str[j]
        else:
            current_sub_str += sub_str[j]
            if len(current_sub_str) != 0:
                sub_str_lst.append(current_sub_str)
                overall_lst.append(sub_str_lst)
            break

max_str = ""
for i in overall_lst:
    if len(i[0]) > len(max_str):
        max_str = i[0]

print("Longest substring in alphabetical order: " + max_str)