# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:43:03 2021

@author: akladke
"""


def genPrimes():
    x = 2
    lst = [1]
    while True:
        count = 0
        for i in lst:
            if x % i != 0:
                count += 1
        if count == len(lst) - 1:
            yield x
            lst.append(x)
        x += 1
     
for num in genPrimes():
     if num > 50:
         break
     print(num)

# =============================================================================
# def mygen(n):
#     x = 2
#     lst = [1]
#     while x < n:
#         count = 0
#         for i in lst:
#             if x % i != 0:
#                 count += 1
#         if count == len(lst) - 1:
#             yield x
#             lst.append(x)
#         x += 1
# 
# for a in mygen(50):
#     print(a)
# =============================================================================