# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:04:10 2021

@author: akladke
"""

import itertools

# Problem 3
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # numbers = [6, 9, 20]
    # result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) == n]
        
    # if len(result) == 0:
    #     return False
    # else:
    #     return True
    #numbers = [6, 9, 20]
    #a, b, c = 0, 0, 0
    #equation = 6*a + 9*b + 20*c
    #return n % 6 == 0 or n % 9 == 0 or n % 15 == 0
    i = 6
    while i <= n:
        if n % i == 0:
            return True
        i += 6
    j = 9
    while j <= n:
        if n % j == 0:
            return True
        j += 9
    k = 15
    while k <= n:
        if n % k == 0:
            return True
        k += 15
    return False

# Problem 4
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    current_longest_inc = []
    mono_increase = []
    for i in range(len(L)):
        if i == 0:
            mono_increase.append(L[i])
            continue
        if L[i] >= L[i - 1]:
            mono_increase.append(L[i])
        else:
            current_longest_inc.append(mono_increase)
            mono_increase = [L[i]]
    # Appends last set of numbers to current_longest_inc
    current_longest_inc.append(mono_increase)
    max_len_inc = max(current_longest_inc, key=len)
    
    current_longest_desc = []
    mono_decrease = []
    for i in range(len(L)):
        if i == 0:
            mono_decrease.append(L[i])
            continue
        if L[i] <= L[i - 1]:
            mono_decrease.append(L[i])
        else:
            current_longest_desc.append(mono_decrease)
            mono_decrease = [L[i]]
    # Appends last set of numbers to current_longest_desc
    current_longest_desc.append(mono_decrease)
    max_len_desc = max(current_longest_desc, key=len)
    
    if len(max_len_inc) > len(max_len_desc):
        return sum(max_len_inc)
    if len(max_len_desc) > len(max_len_inc):
        return sum(max_len_desc)
    if len(max_len_inc) == len(max_len_desc):
        starting_index_inc = 0
        for i in current_longest_inc:
            if i == max_len_inc:
                break
            if i != max_len_inc:
                starting_index_inc += len(i)
        
        starting_index_desc = 0
        for i in current_longest_desc:
            if i == max_len_desc:
                break
            if i != max_len_desc:
                starting_index_desc += len(i)
        
        if starting_index_inc < starting_index_desc:
            return sum(max_len_inc)
        else:
            return sum(max_len_desc)

# Problem 5
def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    map_dict = {}
    for i in range(len(map_from)):
        map_dict[map_from[i]] = map_to[i]
    new_str = ""
    for i in code:
        new_str += map_dict[i]
    return (map_dict, new_str)

# Problem 6 in usresident.py

# Problem 7 in problem7.py