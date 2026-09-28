
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 23/09/2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user

str1=input("What is your favorite ice cream?:")

str2=input("Who is your favorite superhero?:")

if len(str1) > len(str2): 
    print("Statement 1 is longer than Statement 2!")

elif len(str1) < len(str2):
    print("Statement 2 is longer than Statement 1")

else:
    print ("Statement 1 and Statemetn 2 are of equal length!")
    