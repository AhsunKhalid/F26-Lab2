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
        tax = 800 + 0.15 * (income - 8000)
    else:
        tax = 4400 + 0.25 * (income - 32000)

elif status == "married":
    if income <= 16000:
        tax = income *0.10
    elif income <= 64000:
        tax = 1600 + 0.15 * (income - 16000)
    else:
        tax = 8800 + 0.25 * (income - 64000)

else:
    print ("Invalid Status.")
    tax = None

if tax is not None:
    print ("Your tax is: $", round(tax, 2))
    