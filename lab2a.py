# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: AHSUN KHALID
# Date: 23/09/2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py

# TO DO 1: Follow the instructions given in README.md file
x=input("Please input Number:") 

print(type(x))

x=int(x)

if x>= 6:
    print ("x is greater than 6!")

if x>=4 or x<12:
    print ("x is equal to and greater than 4 and less than 12!")