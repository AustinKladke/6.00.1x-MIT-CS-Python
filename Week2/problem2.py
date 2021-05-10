# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:26:04 2021

@author: akladke
"""

# Autogenerated variables for the problem
balance = 3329
annualInterestRate = 0.2

# Variables
initial_balance = balance # Preserves original balance number
monthly_payment = 10
monthly_interest_rate = annualInterestRate/12
month = 0
while balance > 0:
    if month > 11:
        month = 0
        balance = initial_balance
        monthly_payment += 10
    monthly_unpaid_balance = balance - monthly_payment
    balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    month += 1
    #print("Monthly Payment = {}; Month {}:  {}".format(monthly_payment, month, balance))
print("Lowest payment: {}".format(monthly_payment))


