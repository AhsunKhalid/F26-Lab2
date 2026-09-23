# Add comments before you do anything else.

#!/usr/bin/env python3
# Author:
# Date:
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys
#print(sys.argv) # prints the list of all arguments given at the command line when running our python script from terminal.
#print(len(sys.argv)) # tells us the number of command line arguments the user provides from termin
num_args=len(sys.argv)-1
if num_args<2:
    print("The script requires at least 2 arguments, no arguements provided")
else:
    name=sys.argv[1]
    age=sys.argv [2]
    if num_args==2:
        print(f"Hi {name}, good job, you provided two arguements")
    else:
        print(f"Hi {name}, you are {age} years old and the script recieved exactly {num_args} arguements")