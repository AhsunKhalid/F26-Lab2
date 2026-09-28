# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 23/09/2026
# Purpose: Learn how and practice using nested if, elif, and else statments..
# Usage: ./lab2g.py

# TO DO 1: Follow the instructions given in README.md file
# Initialize constant variables for the tax rates and rate limits.

income=float(input("Please enter your income:"))
status=input("Please enter your current marital status:").lower()

if status == "single":
    if income <= 8000:
        tax = income * 0.10
    elif income <= 32000:
        tax = 800 + (income -8000)  *0.15
    else:
        tax = 4400 + (income -32000) * 0.25

elif status == "married":
    if income <= 16000:
        tax = income *0.10
    elif income <= 64000:
        tax = 1600 + (income -16000) *0.15
    else:
        tax = 8800 + (income - 64000) * 0.25

else:
    print ("Invalid Status.")
    tax = None

if tax is not None:
    print ("Your tax is: $", round(tax, 2))