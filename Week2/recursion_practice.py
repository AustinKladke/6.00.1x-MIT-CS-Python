# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:53:57 2021

@author: akladke

Problems:
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-recursion.php
"""

# Problem 1
lst = [10, 10, 25, 100]

def lst_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + lst_sum(lst[1:])
    
# Problem 2

# Problem 3
lst1 = [1, 2, [3,4], [5,6]]

def lst_nested_sum(lst):
    new_lst = []
    for i in lst:
        if isinstance(i, int):
            new_lst.append(i)
        else:
            new_lst.append(lst_nested_sum(i))
    return sum(new_lst)

# Problem 4
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Problem 5

# Problem 6
num = 45

def num_to_lst(num):
    lst = []
    for i in str(num):
        lst.append(int(i))
    return lst

def sum_int_digits(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_int_digits(lst[1:])
    
# Problem 7
num_positive = 10

def nums_lst(num):
    lst = []
    for i in range(num, 0, - 2):
        lst.append(i)
    return lst

def sum_pos_ints(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + sum_pos_ints(lst[1:])
    
# Better solution to Problem 7
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
    
# Problem 8

# Problem 9

# Problem 10
def power_recur(a, b):
    if b == 0:
        return 1
    else:
        return a * power_recur(a, b - 1)
    
# Problem 11

# *** Bonus Problem ***
# Given a number, return the total sum of that number 
# multiplied by every number between 1 and 10. Do not use the 
# sum() built-in function.
#Examples
#multi_sum(1) ➞ 55
# 1 x 1 + 1 x 2 + 1 x 3 ...... 1 x 9 + 1 x 10 = 55

def multi_sum(n, ten = 10):
	# Base case: n * 1 = itself, which is n
	if ten == 1:
		return n
	else:
		# Ex: 1X1 + 1X2
		# (n * ten - 1) + (n * ten - 2) + ...
		# (n * 10) + multi_sum(n, ten - 1)
		# (n * 10) + (n * 9) + ...
		return (n * ten) + multi_sum(n, ten - 1)
    
# Function using recursion that repeats string n number of times
def repeat_string(txt, n):
    if n == 1:
        return txt
    else:
        return txt + repeat_string(txt, n - 1)

# Function using recursion that finds the length of a string
def string_len(txt):
    if txt == "":
        return 0
    else:
        return 1 + string_len(txt[1:])
    
# Function using recursion that finds number of squares in an n * n grid
# Examples: 
    # number_squares(2) --> 5, 
    # number_squares(4) --> 30, 
    # number_squares(5) ---> 55
def number_squares(n):
    if n == 1:
        return 1
    else:
        return n * n + number_squares(n - 1)
    
# Function using recursion that finds the largest integer in a list
def largest_int(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_int = largest_int(lst[1:])
        if max_int > lst[0]:
            return max_int
        else:
            return lst[0]
        
# Print characters of string in reverse order using recursion
def reverse_str(txt):
    if len(txt) == 1:
        return txt[-1]
    else:
        return txt [-1] + reverse_str(txt[:-1])
    
# Print x times multiplication table
def twelve_times(num, times):
    if times == 0:
        return 0
    else:
        print(num)
        return num + twelve_times(num, times - 1)
        