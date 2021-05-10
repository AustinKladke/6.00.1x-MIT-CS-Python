# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 11:40:18 2021

@author: akladke
"""

#balance = 42
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(0, 12):
    min_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - min_payment
    interest = annualInterestRate/12 * unpaid_balance
    balance = round(unpaid_balance + interest, 2)
print("Remaining balance: {}".format(balance))