# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 15:47:53 2021

@author: akladke
"""

# Binary Search Finger Exercise

secret_num = 91
low = 0
high = 100
guess = (high + low) // 2
count = 0

print("Please think of a number between 0 and 100!")
while guess != secret_num:
    guess = (high + low) // 2
    count += 1
    print("Is your secret number {}?".format(guess))
    print("Enter 'h' to indicate the guess is too high.", end = " ")
    print("Enter 'l' to indicate the guess is too low.", end = " ")
    print("Enter 'c' to indicate I guessed correctly.", end = " ")
    indication = input("")
    if indication not in ["h", "l", "c"]:
        print("Sorry I did not understand your input.")
    if indication == "h":
        print("Too high")
        high = guess
    if indication == "l":
        print("Too low")
        low = guess
    if indication == "c":
        print("Correct")
        break
    
print("Game over. Your secret number was: {}".format(guess))
print(count)