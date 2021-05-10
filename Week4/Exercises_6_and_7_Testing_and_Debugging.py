# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 10:30:46 2021

@author: akladke
"""

# Exercise 6
def rem(x, a):
    """
    

    Parameters
    ----------
    x : a non-negative integer argument
    a : a positive integer argument

    Returns
    -------
    integer, the remainder when x is divided by a

    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        return rem(x-a, a) # Error corrected by putting a return in 
                           # front of this statement
   
# Exercise 7
def f(n):
    """
    

    Parameters
    ----------
    n : integer, n >= 0

    Returns
    -------
    integer

    """
    if n == 0:
        return 1
    else:
        return n * f(n - 1)