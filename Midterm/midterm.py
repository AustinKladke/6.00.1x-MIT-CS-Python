# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:38:12 2021

@author: akladke
"""
# Problem 3

def isMyNumber(num):
    secret_num = -25
    #print("Secret number = {}".format(secret_num))
    #print(num)
    if num == secret_num:
        return 0
    if num < secret_num:
        return -1
    if num > secret_num:
        return 1

def jumpAndBackpedal(isMyNumber):
    '''
    isMyNumber: Procedure that hides a secret number. 
     It takes as a parameter one number and returns:
     *  -1 if the number is less than the secret number
     *  0 if the number is equal to the secret number
     *  1 if the number is greater than the secret number
 
    returns: integer, the secret number
    ''' 
    guess = 1
    x = isMyNumber(guess)
    if x == 0:
        return guess
    while x != 0:
        x = isMyNumber(guess)
        if x == 0:
            break
        if x == -1:
            guess += 1
        if x == 1:
            guess -= 1
    return guess
    #foundNumber = False
    #while not foundNumber:
        #sign = isMyNumber
        #if sign == -1:
            #guess *= 2
        #else:
            #guess -= 1
    #return guess
    
# Problem 4
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    total = 0
    for i in range(len(listA)):
        total += listA[i] * listB[i]
    return total

# Problem 5

# Examples
# If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
# If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
# If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    new_dict = {}
    new_dict_1 = {}
    for key, value in d.items():
        new_dict.setdefault(value, list()).append(key)
    for key, value in new_dict.items():
        new_dict_1[key] = sorted(value)
    return new_dict_1

# Problem 6
def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    else:
        return(N % 10) + sumDigits(N // 10)
    
# Problem 7
def satisfiesF(L):
     """
     Assumes L is a list of strings
     Assume function f is already defined for you and it maps a string to a Boolean
     Mutates L such that it contains all of the strings, s, originally in L such
             that f(s) returns True, and no other elements. Remaining elements in L
             should be in the same order.
     Returns the length of L after mutation
     """
     new_lst = []
     for i in L:
         if f(i) == True:
             new_lst.append(i)
     L[:] = new_lst
     return len(L)
 
#run_satisfiesF(L, satisfiesF) 

def f(s):
    return 'a' in s
      
L = ['a', 'b', 'a']
#L = ['b', 'c', 'd', 'a', 'a', 'b', 'c', 'a']
#L = []
print(satisfiesF(L))
print(L)

# Next two lines should be printed:
#2
#['a', 'a']

    
    