# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:18:19 2021

@author: akladke
"""

import math

def polysum(n, s):
    """
    n: int, s:int
    Returns a float of the calculation of the sum of the area of the polygon and the square
    of the perimeter of the regular polygon
    """
    return round((0.25*n*s**2/math.tan(math.pi/n)) + (n * s)**2, 4)