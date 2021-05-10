# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 09:16:58 2021

@author: akladke
"""

# Exact code that was submitted to grader for "Guess my number"
# problem

secret_num = 0
low = 0
high = 100
guess = (high + low) // 2

print("Please think of a number between 0 and 100!")
while guess != secret_num:
    guess = (high + low) // 2
    print("Is your secret number {}?".format(guess))
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    print("Enter 'l' to indicate the guess is too low.", end = " ")
    print("Enter 'c' to indicate I guessed correctly.", end = " ")
    indication = input("")
    if indication not in ["h", "l", "c"]:
        print("Sorry I did not understand your input.")
    if indication == "h":
        high = guess
    if indication == "l":
        low = guess
    if indication == "c":
        break
    
print("Game over. Your secret number was: {}".format(guess))